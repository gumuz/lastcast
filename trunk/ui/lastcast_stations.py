#!/usr/bin/env python

import sys, popen2

from PyQt4 import QtCore, QtGui

# load precompiled ui
from lastcast_stations_ui import Ui_LastcastStationsDialog


class LastcastStationsDialog(QtGui.QDialog, Ui_LastcastStationsDialog):
    def __init__(self, parent):
        QtGui.QMainWindow.__init__(self, parent)

        self.parent = parent

        # Set up the user interface from Designer.
        self.setupUi(self)

        # load stations
        #todo nested stations in folders
        for title, settings in self.parent.config['stations'].items():
            qtwi = QtGui.QTreeWidgetItem()
            qtwi.setText(0, title)
            qtwi.setText(1, settings['hosts'])
            self.treeStations.insertTopLevelItem(0, qtwi)


    #slots
    def addStation(self):
        pass


    def editStation(self):
        pass


    def deleteStation(self):
        pass


    def selectStation(self):
        pass


    def changeSelection(self):
        pass