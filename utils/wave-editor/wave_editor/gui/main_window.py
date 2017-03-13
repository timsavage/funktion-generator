from __future__ import absolute_import

from PySide import QtGui

from .. import wave_functions
from .._ui.main_window import Ui_MainWindow
from .dialogs import AboutDialog
from .wave_editor import WaveDocumentEditor


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
        self.ui.actionCDatatable.triggered.connect(self.exportC)
        self.ui.actionClose.triggered.connect(self.ui.mdiArea.closeAllSubWindows)
        self.ui.actionQuit.triggered.connect(self.action_Quit__triggered)

        self.ui.actionZero.triggered.connect(self.applyZero)
        # Generate
        self.ui.actionSine.triggered.connect(self.applySine)
        self.ui.actionSquare.triggered.connect(self.applySquare)
        self.ui.actionTriangle.triggered.connect(self.applyTriangle)
        self.ui.actionSawtooth.triggered.connect(self.applySawtooth)
        self.ui.actionReverseSawtooth.triggered.connect(self.applyReverseSawtooth)
        # Merge
        self.ui.actionMergeSine.triggered.connect(self.applyMergeSine)
        self.ui.actionMergeSquare.triggered.connect(self.applyMergeSquare)
        self.ui.actionMergeTriangle.triggered.connect(self.applyMergeTriangle)
        self.ui.actionMergeSawtooth.triggered.connect(self.applyMergeSawtooth)
        self.ui.actionMergeReverseSawtooth.triggered.connect(self.applyMergeReverseSawtooth)

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

    def exportC(self):
        if self.activeMdiChild and self.activeMdiChild.exportC():
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
