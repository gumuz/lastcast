#!/usr/bin/env python

import sys, popen2, pprint

from PyQt4 import QtCore, QtGui
from PyQt4 import uic

from stations import StationsDialog

# for debugging purposes
DEBUG = True

if DEBUG:
    # compile resources
    popen2.popen2("pyrcc4 lastcast.qrc > lastcast_rc.py")[0].read()
    popen2.popen2("pyuic4 lastcast2.ui > lastcast_ui.py")[0].read()

    # load ui on the fly
    Ui_MainWindow, base_class = uic.loadUiType("./lastcast2.ui")
else:
    # load precompiled ui
    from lastcast_ui import Ui_MainWindow



class LastCastMain(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        #todo setup config object

        # set up threaded stream reader & player



    def loadStations(self):
        """ Load stations from python file """
        from settings.stations import stations

        # populate tree
        for station in stations['shoutcast']:
            qtwi = QtGui.QTreeWidgetItem()
            qtwi.setText(0, station['title'])
            qtwi.setText(1, ';'.join(station['hosts']))
            self.treeStations.insertTopLevelItem(0, qtwi)

    def saveStations(self):
        """ Save stations in python syntax to stations.py """
        f = open('./settings/stations.py', 'w')
        f.write("stations = %s" % pprint.pformat(stations))
        f.close()


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
        ui = StationsDialog(self)
        ui.exec_()


    def showSettings(self):
        pass



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')

    window = LastCastMain()
    window.show()

    sys.exit(app.exec_())
