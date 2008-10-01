# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stations.ui'
#
# Created: Wed Oct 01 15:50:54 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_StationsDialog(object):
    def setupUi(self, StationsDialog):
        StationsDialog.setObjectName("StationsDialog")
        StationsDialog.resize(419, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ui/resources/ui/transmit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StationsDialog.setWindowIcon(icon)
        StationsDialog.setModal(True)
        self.treeStations = QtGui.QTreeWidget(StationsDialog)
        self.treeStations.setGeometry(QtCore.QRect(10, 55, 401, 176))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeStations.sizePolicy().hasHeightForWidth())
        self.treeStations.setSizePolicy(sizePolicy)
        self.treeStations.setRootIsDecorated(False)
        self.treeStations.setExpandsOnDoubleClick(True)
        self.treeStations.setObjectName("treeStations")
        self.btnStationEdit = QtGui.QToolButton(StationsDialog)
        self.btnStationEdit.setGeometry(QtCore.QRect(60, 5, 50, 45))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ui/resources/ui/transmit_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStationEdit.setIcon(icon1)
        self.btnStationEdit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnStationEdit.setAutoRaise(True)
        self.btnStationEdit.setObjectName("btnStationEdit")
        self.btnStationDelete = QtGui.QToolButton(StationsDialog)
        self.btnStationDelete.setGeometry(QtCore.QRect(110, 5, 50, 45))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ui/resources/ui/transmit_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStationDelete.setIcon(icon2)
        self.btnStationDelete.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnStationDelete.setAutoRaise(True)
        self.btnStationDelete.setObjectName("btnStationDelete")
        self.btnStationAdd = QtGui.QToolButton(StationsDialog)
        self.btnStationAdd.setGeometry(QtCore.QRect(10, 5, 50, 45))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ui/resources/ui/transmit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStationAdd.setIcon(icon3)
        self.btnStationAdd.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnStationAdd.setAutoRaise(True)
        self.btnStationAdd.setObjectName("btnStationAdd")
        self.btnClose = QtGui.QPushButton(StationsDialog)
        self.btnClose.setGeometry(QtCore.QRect(335, 240, 75, 23))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(StationsDialog)
        QtCore.QObject.connect(self.btnStationAdd, QtCore.SIGNAL("clicked()"), StationsDialog.addStation)
        QtCore.QObject.connect(self.btnStationEdit, QtCore.SIGNAL("clicked()"), StationsDialog.editStation)
        QtCore.QObject.connect(self.btnStationDelete, QtCore.SIGNAL("clicked()"), StationsDialog.deleteStation)
        QtCore.QObject.connect(self.btnClose, QtCore.SIGNAL("clicked()"), StationsDialog.accept)
        QtCore.QObject.connect(self.treeStations, QtCore.SIGNAL("itemSelectionChanged()"), StationsDialog.changeSelection)
        QtCore.QObject.connect(self.treeStations, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"), StationsDialog.selectStation)
        QtCore.QMetaObject.connectSlotsByName(StationsDialog)

    def retranslateUi(self, StationsDialog):
        StationsDialog.setWindowTitle(QtGui.QApplication.translate("StationsDialog", "Stations", None, QtGui.QApplication.UnicodeUTF8))
        self.treeStations.setSortingEnabled(True)
        self.treeStations.headerItem().setText(0, QtGui.QApplication.translate("StationsDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeStations.headerItem().setText(1, QtGui.QApplication.translate("StationsDialog", "Hosts", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStationEdit.setText(QtGui.QApplication.translate("StationsDialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStationDelete.setText(QtGui.QApplication.translate("StationsDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStationAdd.setText(QtGui.QApplication.translate("StationsDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("StationsDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

import lastcast_rc
