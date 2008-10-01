#!/usr/bin/env python

import sys, popen2

from PyQt4 import QtCore, QtGui
from PyQt4 import uic


# for debugging purposes
DEBUG = True

if DEBUG:
    # compile resources
    popen2.popen2("pyrcc4 lastcast.qrc > lastcast_rc.py")[0].read()
    popen2.popen2("pyuic4 stations.ui > stations_ui.py")[0].read()

    # load ui on the fly
    Ui_StationsDialog, base_class = uic.loadUiType("./stations.ui")
else:
    # load precompiled ui
    from stations_ui import Ui_StationsDialog


class StationsDialog(QtGui.QDialog, Ui_StationsDialog):
    def __init__(self, parent):
        QtGui.QMainWindow.__init__(self, parent)

        # Set up the user interface from Designer.
        self.setupUi(self)


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