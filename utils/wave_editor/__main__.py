from __future__ import absolute_import
import sys

from PySide.QtGui import *

from wave_editor._ui import Ui_MainWindow, Ui_editorPanel

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_Quit.triggered.connect(self.action_Quit__triggered)

    def action_Quit__triggered(self):
        app.exit()
    

def main():
    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()

