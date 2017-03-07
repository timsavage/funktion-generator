from __future__ import absolute_import
import sys

from PySide.QtGui import *

from wave_editor._ui.main_window import Ui_MainWindow
from wave_editor._ui.wave_editor import Ui_EditorWindow

app = QApplication(sys.argv)


class EditorPanel(QMdiSubWindow):
    def __init__(self, parent):
        super(EditorPanel, self).__init__(parent)
        self.ui = Ui_EditorWindow()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_Quit.triggered.connect(self.action_Quit__triggered)

        self._editors = []
        editor = EditorPanel(self)
        self._editors.append(editor)
        self.ui.mdiArea.addSubWindow(editor)
        editor.show()

    def action_Quit__triggered(self):
        app.exit()
    

def main():
    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()

