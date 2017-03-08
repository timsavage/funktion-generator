from __future__ import absolute_import
import sys

from PySide import QtCore, QtGui

from wave_editor._ui.main_window import Ui_MainWindow
from wave_editor._ui.wave_editor import Ui_EditorWindow
from wave_editor._ui.about_dialog import Ui_AboutDialog

app = QtGui.QApplication(sys.argv)


class AboutDialog(QtGui.QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)


class WaveDocumentEditor(QtGui.QGraphicsView):
    sequenceNumber = 0

    def __init__(self):
        super(WaveDocumentEditor, self).__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.isUntitled = True

    def newFile(self):
        self.isUntitled = True
        WaveDocumentEditor.sequenceNumber += 1
        self.currentFile = "wave{}.wave".format(self.sequenceNumber)
        self.setWindowTitle(self.currentFile + "[*]")

    def loadFile(self, file_name):
        file = QtCore.QFile(file_name)
        if not file.open(QtCore.QFile.ReadOnly):
            QtGui.QMessageBox.warning(self, "Wave Editor", "Cannot read file: {}\n{}".format(
                file_name, file.errorString()
            ))
            return False

        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        # Load data
        QtGui.QApplication.restoreOverrideCursor()

        self.setCurrentFile(file_name)

        return True


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_New.triggered.connect(self.newFile)
        self.ui.action_Open.triggered.connect(self.openFile)
        self.ui.action_Quit.triggered.connect(self.action_Quit__triggered)
        self.ui.action_About.triggered.connect(self.action_About__triggered)

        self.newFile()

    def createEditorChild(self):
        child = WaveDocumentEditor()
        self.ui.mdiArea.addSubWindow(child)
        return child

    def newFile(self):
        child = self.createEditorChild()
        child.newFile()
        child.show()

    def openFile(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Open wave table...", "*.wave|Wave table")
        if file_name:
            child = self.createEditorChild()
            child.loadFile(file_name)
            child.show()

    def action_Quit__triggered(self):
        app.exit()

    def action_About__triggered(self):
        AboutDialog().exec_()


def main():
    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()

