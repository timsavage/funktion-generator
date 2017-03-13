from __future__ import absolute_import
import sys

from PySide import QtGui

from wave_editor.gui.main_window import MainWindow

app = QtGui.QApplication(sys.argv)


def main():
    # Show main window
    main_window = MainWindow()
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()
