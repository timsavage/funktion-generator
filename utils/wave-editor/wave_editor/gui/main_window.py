from __future__ import absolute_import

from PySide import QtGui

from .. import wave_functions
from .._ui.main_window import Ui_MainWindow
from .dialogs import AboutDialog
from .wave_editor import WaveDocumentEditor


class MainWindow(QtGui.QMainWindow):
    def __init__(self, devices, parent=None):
        super(MainWindow, self).__init__(parent)

        self.devices = devices
        self.devices.serviceAdd.connect(self.addDevice)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # File
        self.ui.actionNew.triggered.connect(self.newFile)
        self.ui.actionNew2.triggered.connect(self.newFile)
        self.ui.actionNew2.setIcon(QtGui.QIcon.fromTheme('document-new'))
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionOpen2.triggered.connect(self.openFile)
        self.ui.actionOpen2.setIcon(QtGui.QIcon.fromTheme('document-open'))
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSave2.triggered.connect(self.save)
        self.ui.actionSave2.setIcon(QtGui.QIcon.fromTheme('document-save'))
        self.ui.actionSaveAs.triggered.connect(self.saveAs)
        self.ui.actionASMDataTable.triggered.connect(self.exportAsm)
        self.ui.actionCDatatable.triggered.connect(self.exportC)
        self.ui.actionClose.triggered.connect(self.ui.mdiArea.closeAllSubWindows)
        self.ui.actionQuit.triggered.connect(self.quit)
        # Edit
        self.ui.actionUndo.triggered.connect(self.undo)
        self.ui.actionUndo2.triggered.connect(self.undo)
        self.ui.actionUndo2.setIcon(QtGui.QIcon.fromTheme('edit-undo'))
        # View
        self.ui.actionIncrease.triggered.connect(self.zoomIn)
        self.ui.actionDecrease.triggered.connect(self.zoomOut)
        # Generate
        self.ui.actionZero.triggered.connect(self.applyZero)
        self.ui.actionSine.triggered.connect(self.applySine)
        self.ui.actionSquare.triggered.connect(self.applySquare)
        self.ui.actionTriangle.triggered.connect(self.applyTriangle)
        self.ui.actionSawtooth.triggered.connect(self.applySawtooth)
        self.ui.actionReverseSawtooth.triggered.connect(self.applyReverseSawtooth)
        self.ui.actionNoise.triggered.connect(self.applyNoise)
        # Merge
        self.ui.actionMergeSine.triggered.connect(self.applyMergeSine)
        self.ui.actionMergeSquare.triggered.connect(self.applyMergeSquare)
        self.ui.actionMergeTriangle.triggered.connect(self.applyMergeTriangle)
        self.ui.actionMergeSawtooth.triggered.connect(self.applyMergeSawtooth)
        self.ui.actionMergeRSawtooth.triggered.connect(self.applyMergeReverseSawtooth)
        self.ui.actionMergeNoise.triggered.connect(self.applyMergeNoise)
        # Tools
        self.ui.actionInvert.triggered.connect(self.invertWave)
        self.ui.actionInvert2.triggered.connect(self.invertWave)
        self.ui.actionMirror.triggered.connect(self.mirrorWave)
        self.ui.actionMirror2.triggered.connect(self.mirrorWave)
        self.ui.actionRectify.triggered.connect(self.rectifyWave)
        self.ui.actionRectify2.triggered.connect(self.rectifyWave)
        self.ui.actionCentre.triggered.connect(self.centreWave)
        self.ui.actionCentre2.triggered.connect(self.centreWave)
        self.ui.actionNormalise.triggered.connect(self.normaliseWave)
        self.ui.actionNormalise2.triggered.connect(self.normaliseWave)
        # About
        self.ui.actionAbout.triggered.connect(self.showAbout)

        self.newFile()

    def closeEvent(self, event):
        self.ui.mdiArea.closeAllSubWindows()
        if self.activeMdiChild:
            event.ignore()
        else:
            # self.writeSettings()
            event.accept()

    def addDevice(self, name):
        pass

    def newFile(self):
        child = WaveDocumentEditor()
        self.ui.mdiArea.addSubWindow(child)
        child.newFile()
        child.show()

    def openFile(self):
        file_name, _ = QtGui.QFileDialog.getOpenFileName(self, "Open wave table...", "*.wave|Wave table")
        if file_name:
            child = WaveDocumentEditor()
            if child.loadFile(file_name):
                self.ui.mdiArea.addSubWindow(child)
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

    def exportC(self):
        if self.activeMdiChild and self.activeMdiChild.exportC():
            self.statusBar().showMessage("File exported", 2000)

    def closeWindow(self):
        if self.activeMdiChild and self.activeMdiChild.saveAs():
            self.statusBar().showMessage("File saved", 2000)

    def quit(self):
        QtGui.QApplication.quit()

    def undo(self):
        if self.activeMdiChild:
            self.activeMdiChild.undo()

    def zoomIn(self):
        if self.activeMdiChild:
            self.activeMdiChild.zoomIn()

    def zoomOut(self):
        if self.activeMdiChild:
            self.activeMdiChild.zoomOut()

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

    def applyNoise(self):
        if self.activeMdiChild:
            self.activeMdiChild.generateWave(wave_functions.noise)

    def applyMergeSine(self):
        if self.activeMdiChild:
            self.activeMdiChild.mergeWave(wave_functions.sine_wave)

    def applyMergeSquare(self):
        if self.activeMdiChild:
            self.activeMdiChild.mergeWave(wave_functions.square_wave)

    def applyMergeTriangle(self):
        if self.activeMdiChild:
            self.activeMdiChild.mergeWave(wave_functions.triangle_wave)

    def applyMergeSawtooth(self):
        if self.activeMdiChild:
            self.activeMdiChild.mergeWave(wave_functions.sawtooth_wave)

    def applyMergeReverseSawtooth(self):
        if self.activeMdiChild:
            self.activeMdiChild.mergeWave(wave_functions.reverse_sawtooth_wave)

    def applyMergeNoise(self):
        if self.activeMdiChild:
            self.activeMdiChild.mergeWave(wave_functions.noise)

    def mirrorWave(self):
        if self.activeMdiChild:
            self.activeMdiChild.applyFunction(wave_functions.mirror_wave)

    def invertWave(self):
        if self.activeMdiChild:
            self.activeMdiChild.applyFunction(wave_functions.invert_wave)

    def centreWave(self):
        if self.activeMdiChild:
            self.activeMdiChild.applyFunction(wave_functions.centre_wave)

    def normaliseWave(self):
        if self.activeMdiChild:
            self.activeMdiChild.applyFunction(wave_functions.normalise_wave)

    def rectifyWave(self):
        if self.activeMdiChild:
            self.activeMdiChild.applyFunction(wave_functions.rectify_wave)

    def showAbout(self):
        AboutDialog().exec_()

    @property
    def activeMdiChild(self):
        active_sub_window = self.ui.mdiArea.activeSubWindow()
        if active_sub_window:
            return active_sub_window.widget()
