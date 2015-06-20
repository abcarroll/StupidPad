import sys
import webbrowser
from PyQt4 import QtGui

from interface.Interface import Ui_MainWindow


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect our signals with our slots
        self.ui.btnOpen.clicked.connect(self.OpenDialog)
        self.ui.actionOpen.triggered.connect(self.OpenDialog)
        self.ui.btnSave.clicked.connect(self.SaveDialog)
        self.ui.actionSave.triggered.connect(self.SaveDialog)
        self.ui.btnSave.clicked.connect(self.SaveDialog)
        self.ui.actionSave.triggered.connect(self.SaveDialog)
        self.ui.btnSaveAs.clicked.connect(self.SaveAsDialog)
        self.ui.actionSaveAs.triggered.connect(self.SaveAsDialog)
        self.ui.actionPornhub.triggered.connect(self.OpenPornhub)
        self.ui.actionPythonOrg.triggered.connect(self.OpenPythonOrg)

    def OpenDialog(self):
        fileDialog = QtGui.QFileDialog(self)
        self.fileName = fileDialog.getOpenFileName()
        from os.path import isfile

        if isfile(self.fileName):
            fileBuffer = open(self.fileName).read()
            self.ui.textEditor.setText(fileBuffer)
            self.ui.statusBar.setStatusTip("Currently editing file " + self.fileName)

    def SaveDialog(self):
        filePointer = open(self.fileName, 'w+')
        filePointer.write(self.ui.textEditor.toPlainText());
        filePointer.close()
        self.ui.statusBar.setStatusTip("Currently editing file " + self.fileName)

    def SaveAsDialog(self):
        fileDialog = QtGui.QFileDialog(self)
        self.fileName = fileDialog.getSaveFileName()
        filePointer = open(self.fileName, 'w+')
        filePointer.write(self.ui.textEditor.toPlainText());
        filePointer.close()
        self.ui.statusBar.setStatusTip("Currently editing file " + self.fileName)

    def OpenPornhub(self):
        webbrowser.open("https://www.pornhub.com")

    def OpenPythonOrg(self):
        webbrowser.open("https://www.python.org")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myApp = StartQT4()
    myApp.show()
    sys.exit(app.exec_())
