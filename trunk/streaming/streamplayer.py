#!/usr/bin/env python
import urllib2

import pymedia.muxer as muxer
import pymedia.audio.acodec as acodec
import pymedia.audio.sound as sound

dm= muxer.Demuxer('mp3')

class StreamPlayer(object):
    def __init__(self, volume=32768):
        
        self.dec = self.snd = None
        self.volume = volume
        
    def setVolume(self, volume):
        self.volume = volume
        
    def play(self, streamdata):
        self.isplaying = True
        
        for frame in  dm.parse(streamdata):
            # Assume for now only audio streams
            if not self.isplaying: break
            
            if self.dec == None:
                self.dec = acodec.Decoder(dm.streams[frame[0]])
           
            raw = self.dec.decode(frame[1])
            if raw and raw.data:
                if self.snd == None:
                    self.snd = sound.Output(int(raw.sample_rate), raw.channels, sound.AFMT_S16_LE, 0)
             
            data = raw.data
            self.snd.setVolume(self.volume)
            self.snd.play(data)
 
    def stop(self):
        self.isplaying = False
        if self.snd: self.snd.stop()

