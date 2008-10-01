#!/usr/bin/env python

import sys, popen2

from PyQt4 import QtCore, QtGui
from configobj import ConfigObj

# load precompiled ui
from lastcast_main_ui import Ui_LastcastMainWindow

# load stations dialog
from lastcast_stations import LastcastStationsDialog

class LastcastMainWindow(QtGui.QMainWindow, Ui_LastcastMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        # load config
        self.config = ConfigObj('lastcast.ini')

        # set up threaded stream reader & player

        # status
        self.setStatus('Lastcast started')


    def setStatus(self, msg):
        self.statusBar.showMessage(msg)


    # slots
    def play(self):
        pass


    def stop(self):
        pass


    def record(self):
        pass


    def love(self):
        pass


    def ban(self):
        pass


    def volumeChanged(self, value):
        pass


    def showStations(self):
        ui = LastcastStationsDialog(self)
        ui.exec_()


    def showSettings(self):
        pass