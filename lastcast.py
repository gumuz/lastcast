#!/usr/bin/env python

import sys, popen2, pprint

from PyQt4 import QtCore, QtGui
from PyQt4 import uic


# compile and load ui
popen2.popen2("pyrcc4 ./ui/lastcast.qrc > ./ui/lastcast_rc.py")
popen2.popen2("pyuic4 ./ui/lastcast_main.ui > ./ui/lastcast_main_ui.py")
popen2.popen2("pyuic4 ./ui/lastcast_stations.ui > ./ui/lastcast_stations_ui.py")

from ui.lastcastmain import MainWindow


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle('cleanlooks')

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
