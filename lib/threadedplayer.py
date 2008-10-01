#!/usr/bin/env python

from PyQt4.QtCore import *

from shoutcast import ShoutCastClient
from streamplayer import StreamPlayer

class ThreadedPlayer(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        
        self.isplaying = False
        self.title = ''
        
        self.host = None
        self.streamplayer = StreamPlayer()
        
    def __del__(self):
        if self.host: self.host.disconnect()
        self.terminate()
    
    def setHosts(self, hosts):
        tmp = self.isplaying
        self.stop()    
        
        if self.host: self.host.disconnect()
        
        self.host = ShoutCastClient(hosts)
        self.host.connect()
        
        if tmp: self.play()
        
    def checkMetadata(self):
        metadata = self.host.getMetadata()
        title = metadata.get('StreamTitle', '')
        
        if title != self.title:
            self.title = title
            self.emit(SIGNAL("titleChanged(QString)"), title)
        
    def play(self):
        self.isplaying = True
        
    def stop(self):
        self.isplaying = False
        self.streamplayer.stop()
        
    def setVolume(self, value):
        self.streamplayer.setVolume(value)
    
    def run(self):
        while True:
            if self.isplaying:
                try:
                    data = self.host.read(512)
                    self.streamplayer.play(data)
                except:
                    pass
                
                self.checkMetadata()