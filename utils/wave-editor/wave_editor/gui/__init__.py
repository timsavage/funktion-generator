from __future__ import absolute_import

from PySide import QtCore, QtGui

from .. import wave_functions
from ..wave_file import WaveTable
from .._ui.main_window import Ui_MainWindow
from .dialogs import AboutDialog, AsmExportDialog
from .widgets import WaveScene


class WaveDocumentEditor(QtGui.QGraphicsView):
    sequence_number = 0

    def __init__(self):
        super(WaveDocumentEditor, self).__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.isUntitled = True
        self.fileName = None
        self.waveTable = None
        self.scene = None

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def newFile(self):
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
        f = QtCore.QFile(file_name)
        if not f.open(QtCore.QFile.ReadOnly):
            QtGui.QMessageBox.warning(self, "Wave Editor", "Cannot read file: {}\n{}".format(
                file_name, f.errorString()
            ))
            return False

        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.waveTable = WaveTable.read(f)
        self.setFileName(file_name)
        self.scene = WaveScene(self.waveTable)
        self.setScene(self.scene)
        self.fileChanged()
        QtGui.QApplication.restoreOverrideCursor()

        return True

    def save(self):
        if self.isUntitled:
            return self.saveAs()
        else:
            return self.saveFile(self.fileName)

    def saveAs(self):
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
        self.waveTable.insert(function())
        self.fileChanged()
        # self.setTransform(QtGui.QTransform.fromScale(2, 2))

    def mirrorWave(self):
        self.waveTable.mirror()
        self.fileChanged()

    def invertWave(self):
        self.waveTable.invert()
        self.fileChanged()

    def exportAsm(self):
        output_file = QtCore.QFileInfo(self.fileName).baseName()
        asmStyle, asmLabel = AsmExportDialog.getExportOptions(None, output_file)
        if not asmLabel:
            return

        file_name, _ = QtGui.QFileDialog.getSaveFileName(self, "Export As...", output_file + '.asm')
        if file_name:
            f = QtCore.QFile(file_name)
            if not f.open(QtCore.QFile.WriteOnly):
                QtGui.QMessageBox.warning(self, "Wave Editor", "Cannot write file: {}\n{}".format(
                    file_name, f.errorString()
                ))

            QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.waveTable.export_gcc_asm(asmLabel, f)
            QtGui.QApplication.restoreOverrideCursor()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNew.triggered.connect(self.newFile)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSaveAs.triggered.connect(self.saveAs)
        self.ui.actionASMDataTable.triggered.connect(self.exportAsm)
        self.ui.actionClose.triggered.connect(self.ui.mdiArea.closeAllSubWindows)
        self.ui.actionQuit.triggered.connect(self.action_Quit__triggered)

        self.ui.actionZero.triggered.connect(self.applyZero)
        self.ui.actionSine.triggered.connect(self.applySine)
        self.ui.actionSquare.triggered.connect(self.applySquare)
        self.ui.actionTriangle.triggered.connect(self.applyTriangle)
        self.ui.actionSawtooth.triggered.connect(self.applySawtooth)
        self.ui.actionReverseSawtooth.triggered.connect(self.applyReverseSawtooth)

        self.ui.actionInvert.triggered.connect(self.invertWave)
        self.ui.actionMirror.triggered.connect(self.mirrorWave)

        self.ui.actionAbout.triggered.connect(self.action_About__triggered)

        self.newFile()

    def closeEvent(self, event):
        self.ui.mdiArea.closeAllSubWindows()
        if self.activeMdiChild:
            event.ignore()
        else:
            # self.writeSettings()
            event.accept()

    def createEditorChild(self):
        child = WaveDocumentEditor()
        self.ui.mdiArea.addSubWindow(child)
        return child

    def newFile(self):
        child = self.createEditorChild()
        child.newFile()
        child.show()

    def openFile(self):
        file_name, _ = QtGui.QFileDialog.getOpenFileName(self, "Open wave table...", "*.wave|Wave table")
        if file_name:
            child = self.createEditorChild()
            child.loadFile(file_name)
            child.show()

    def save(self):
        if self.activeMdiChild and self.activeMdiChild.save():
            self.statusBar().showMessage("File saved", 2000)

    def saveAs(self):
        if self.activeMdiChild and self.activeMdiChild.saveAs():
            self.statusBar().showMessage("File saved", 2000)

    def exportAsm(self):
        if self.activeMdiChild and self.activeMdiChild.exportAsm():
            self.statusBar().showMessage("File exported", 2000)

    def closeWindow(self):
        if self.activeMdiChild and self.activeMdiChild.saveAs():
            self.statusBar().showMessage("File saved", 2000)

    def action_Quit__triggered(self):
        QtGui.QApplication.quit()

    def applyZero(self):
        if self.activeMdiChild:
            self.activeMdiChild.generateWave(wave_functions.zero_wave)

    def applySine(self):
        if self.activeMdiChild:
            self.activeMdiChild.generateWave(wave_functions.sine_wave)

    def applySquare(self):
        if self.activeMdiChild:
            self.activeMdiChild.generateWave(wave_functions.square_wave)

    def applyTriangle(self):
        if self.activeMdiChild:
            self.activeMdiChild.generateWave(wave_functions.triangle_wave)

    def applySawtooth(self):
        if self.activeMdiChild:
            self.activeMdiChild.generateWave(wave_functions.sawtooth_wave)

    def applyReverseSawtooth(self):
        if self.activeMdiChild:
            self.activeMdiChild.generateWave(wave_functions.reverse_sawtooth_wave)

    def mirrorWave(self):
        if self.activeMdiChild:
            self.activeMdiChild.mirrorWave()

    def invertWave(self):
        if self.activeMdiChild:
            self.activeMdiChild.invertWave()

    def action_About__triggered(self):
        AboutDialog().exec_()

    @property
    def activeMdiChild(self):
        active_sub_window = self.ui.mdiArea.activeSubWindow()
        if active_sub_window:
            return active_sub_window.widget()
