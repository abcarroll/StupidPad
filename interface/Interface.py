# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1101, 841)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout_2.addWidget(self.btnSave, 3, 0, 1, 1)
        self.btnClose = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setAutoDefault(False)
        self.btnClose.setDefault(False)
        self.btnClose.setFlat(False)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))
        self.gridLayout_2.addWidget(self.btnClose, 5, 0, 1, 1)
        self.btnOpen = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpen.sizePolicy().hasHeightForWidth())
        self.btnOpen.setSizePolicy(sizePolicy)
        self.btnOpen.setObjectName(_fromUtf8("btnOpen"))
        self.gridLayout_2.addWidget(self.btnOpen, 2, 0, 1, 1)
        self.textEditor = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        self.textEditor.setFont(font)
        self.textEditor.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEditor.setMouseTracking(True)
        self.textEditor.setAcceptDrops(False)
        self.textEditor.setFrameShape(QtGui.QFrame.Panel)
        self.textEditor.setAcceptRichText(False)
        self.textEditor.setObjectName(_fromUtf8("textEditor"))
        self.gridLayout_2.addWidget(self.textEditor, 0, 0, 1, 1)
        self.btnSaveAs = QtGui.QPushButton(self.centralwidget)
        self.btnSaveAs.setObjectName(_fromUtf8("btnSaveAs"))
        self.gridLayout_2.addWidget(self.btnSaveAs, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.MenuBar = QtGui.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 1101, 19))
        self.MenuBar.setObjectName(_fromUtf8("MenuBar"))
        self.menuFile = QtGui.QMenu(self.MenuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menu_Cool_Stuff = QtGui.QMenu(self.MenuBar)
        self.menu_Cool_Stuff.setObjectName(_fromUtf8("menu_Cool_Stuff"))
        MainWindow.setMenuBar(self.MenuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setEnabled(True)
        self.statusBar.setToolTip(_fromUtf8(""))
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionPornhub = QtGui.QAction(MainWindow)
        self.actionPornhub.setObjectName(_fromUtf8("actionPornhub"))
        self.actionPythonOrg = QtGui.QAction(MainWindow)
        self.actionPythonOrg.setObjectName(_fromUtf8("actionPythonOrg"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menu_Cool_Stuff.addAction(self.actionPornhub)
        self.menu_Cool_Stuff.addAction(self.actionPythonOrg)
        self.MenuBar.addAction(self.menuFile.menuAction())
        self.MenuBar.addAction(self.menu_Cool_Stuff.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Stupid Pad++", None))
        self.btnSave.setText(_translate("MainWindow", "Save File", None))
        self.btnClose.setText(_translate("MainWindow", "Exit Application", None))
        self.btnOpen.setText(_translate("MainWindow", "Open File", None))
        self.btnSaveAs.setText(_translate("MainWindow", "Save File As", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menu_Cool_Stuff.setTitle(_translate("MainWindow", "&Cool Stuff", None))
        self.statusBar.setStatusTip(_translate("MainWindow", "Ready...", None))
        self.actionOpen.setText(_translate("MainWindow", "&Open File...", None))
        self.actionClose.setText(_translate("MainWindow", "E&xit ", None))
        self.actionSaveAs.setText(_translate("MainWindow", "S&ave As...", None))
        self.actionSave.setText(_translate("MainWindow", "&Save", None))
        self.actionPornhub.setText(_translate("MainWindow", "&Pornhub.com", None))
        self.actionPythonOrg.setText(_translate("MainWindow", "P&ython.org", None))
