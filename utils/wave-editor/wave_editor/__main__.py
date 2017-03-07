from __future__ import absolute_import
import sys

from PySide import QtCore, QtGui

from wave_editor._ui.main_window import Ui_MainWindow
from wave_editor._ui.wave_editor import Ui_EditorWindow

app = QtGui.QApplication(sys.argv)


class WaveDocumentEditor(QtGui.QGraphicsView):
    sequenceNumber = 0

    def __init__(self):
        super(WaveDocumentEditor, self).__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.isUntitled = True

    def newFile(self):
        self.isUntitled = True
        self.sequenceNumber += 1
        self.currentFile = "wave{}.wave".format(self.sequenceNumber)
        self.setWindowTitle(self.currentFile + "[*]")

        self.document().contentsChanged.connect(self.documentWasModified)

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
        self.document().contentsChanged.connect(self.documentWasModified)

        return True


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_Quit.triggered.connect(self.action_Quit__triggered)

        child = self.createEditorChild()
        child.show()

    def createEditorChild(self):
        child = WaveDocumentEditor()
        self.ui.mdiArea.addSubWindow(child)
        return child

    def action_Quit__triggered(self):
        app.exit()
    

def main():
    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()

