from __future__ import absolute_import

from PySide import QtCore, QtGui

from ..wave_file import WaveTable, WaveFileError, ExportAsmFormatter, ExportCFormatter
from .dialogs import AsmExportDialog
from .widgets import WaveScene


class WaveDocumentEditor(QtGui.QGraphicsView):
    """
    Individual wave editor documents.
    """
    sequence_number = 0
    wheel_step = 120

    def __init__(self):
        super(WaveDocumentEditor, self).__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.isUntitled = True
        self.fileName = None
        self.waveTable = None
        self.scene = None
        self.undoBuffer = []

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def wheelEvent(self, event):
        if event.modifiers() == QtCore.Qt.ControlModifier:
            delta = event.delta()
            if delta > 0:
                self.zoomIn()
            elif delta < 0:
                self.zoomOut()
        else:
            super(WaveDocumentEditor, self).wheelEvent(event)

    def newFile(self):
        """
        Create a new file
        """
        self.isUntitled = True
        WaveDocumentEditor.sequence_number += 1
        self.fileName = "wave{}.wave".format(self.sequence_number)
        self.waveTable = WaveTable()
        self.scene = WaveScene(self.waveTable)
        self.setScene(self.scene)
        self.fileChanged()
        self.setWindowTitle(self.fileName + "[*]")
        return True

    def loadFile(self, file_name):
        """
        Load an existing wave file.
        
        :param file_name: The name of the file to load. 
        :return: True if successful; else False
         
        """
        f = QtCore.QFile(file_name)
        if not f.open(QtCore.QFile.ReadOnly):
            QtGui.QMessageBox.warning(self, "Wave Editor", "Cannot read file: {}\n{}".format(
                file_name, f.errorString()
            ))
            return False

        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        try:
            self.waveTable = WaveTable.read(f)
            self.setFileName(file_name)
            self.scene = WaveScene(self.waveTable)
            self.setScene(self.scene)
            self.fileChanged()
        except WaveFileError as ex:
            QtGui.QApplication.restoreOverrideCursor()
            QtGui.QMessageBox.warning(self, "Wave Editor", "Invalid wave file: {}\n{}".format(
                file_name, ex
            ))
            return False
        finally:
            QtGui.QApplication.restoreOverrideCursor()

        return True

    def save(self):
        """
        Save the current file (will call save as if not previously saved)
        
        :return: True if successful; else False
        
        """
        if self.isUntitled:
            return self.saveAs()
        else:
            return self.saveFile(self.fileName)

    def saveAs(self):
        """
        Save the current wave to a file as a named selected by the user.
        
        :return: True if successful; else False
         
        """
        file_name, _ = QtGui.QFileDialog.getSaveFileName(self, "Save As...", self.fileName)
        if not file_name:
            return False
        return self.saveFile(file_name)

    def saveFile(self, file_name):
        f = QtCore.QFile(file_name)
        if not f.open(QtCore.QFile.WriteOnly):
            QtGui.QMessageBox.warning(self, "Wave Editor", "Cannot write file: {}\n{}".format(
                file_name, f.errorString()
            ))

        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.waveTable.write(f)
        QtGui.QApplication.restoreOverrideCursor()

        self.setFileName(file_name)
        self.waveTable.clear_modified()

    def maybeSave(self):
        if self.waveTable.modified:
            ret = QtGui.QMessageBox.warning(
                self, "Wave Editor",
                "'{}' has been modified.\nDo you want to save your "
                "changes?".format(QtCore.QFileInfo(self.fileName).fileName()),
                QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel
            )
            if ret == QtGui.QMessageBox.Save:
                return self.save()
            elif ret == QtGui.QMessageBox.Cancel:
                return False

        return True

    def setFileName(self, file_name):
        file_info = QtCore.QFileInfo(file_name)
        self.fileName = file_info.canonicalFilePath()
        self.isUntitled = False
        self.setWindowModified(False)
        self.setWindowTitle(file_info.fileName() + "[*]")

    def fileChanged(self):
        self.setWindowModified(self.waveTable.modified)
        self.scene.render()

    def generateWave(self, function):
        self.undoBuffer.append(list(self.waveTable))
        self.waveTable.insert(function())
        self.fileChanged()

    def mergeWave(self, function):
        self.undoBuffer.append(list(self.waveTable))
        self.waveTable.merge(function())
        self.fileChanged()

    def applyFunction(self, function):
        self.undoBuffer.append(list(self.waveTable))
        self.waveTable.insert(function(self.waveTable))
        self.fileChanged()

    def zoomIn(self):
        self.scale(1.25, 1.25)

    def zoomOut(self):
        self.scale(0.8, 0.8)

    def undo(self):
        """
        Undo the last action performed on the wave. 
        """
        if self.undoBuffer:
            wave = self.undoBuffer.pop()
            self.waveTable.insert(wave)
            self.fileChanged()

    def exportAsm(self):
        """
        Export wave table to ASM file
        """
        output_file = QtCore.QFileInfo(self.fileName).baseName()
        asmStyle, asmLabel = AsmExportDialog.getExportOptions(None, output_file)
        if not asmLabel:
            return

        file_name, _ = QtGui.QFileDialog.getSaveFileName(self, "Export ASM as...", output_file + '.asm')
        if file_name:
            f = QtCore.QFile(file_name)
            if not f.open(QtCore.QFile.WriteOnly):
                QtGui.QMessageBox.warning(self, "Wave Editor", "Cannot write file: {}\n{}".format(
                    file_name, f.errorString()
                ))

            QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            ExportAsmFormatter(self.waveTable, asmLabel, asmStyle)(f)
            QtGui.QApplication.restoreOverrideCursor()

    def exportC(self):
        """
        Export wave table to C file
        """
        output_file = QtCore.QFileInfo(self.fileName).baseName()
        file_name, _ = QtGui.QFileDialog.getSaveFileName(self, "Export C as...", output_file + '.c')
        if file_name:
            f = QtCore.QFile(file_name)
            if not f.open(QtCore.QFile.WriteOnly):
                QtGui.QMessageBox.warning(self, "Wave Editor", "Cannot write file: {}\n{}".format(
                    file_name, f.errorString()
                ))

            QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            ExportCFormatter(self.waveTable, output_file)(f)
            QtGui.QApplication.restoreOverrideCursor()
