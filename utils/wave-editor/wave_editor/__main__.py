from __future__ import absolute_import
import sys

from PySide import QtGui

from wave_editor.gui.main_window import MainWindow
from wave_editor.devices.discovery import Devices

app = QtGui.QApplication(sys.argv)


def main():
    devices = Devices()

    # Show main window
    main_window = MainWindow(devices)
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    main()
