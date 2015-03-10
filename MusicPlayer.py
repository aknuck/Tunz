#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A class to be run in another thread to play the music
#Because of the way PyGame does queueing and checking if song ends, it needs to be running in another thread
#It will loop to check if the current song ended to as to queue the next appropriate song (only one song can be queued at a time)
class MusicPlayer:

    def __init__(self,lib):
        self.library = lib


    def play(sself,song):
        print ""

    def queue(self,song):
        print ""

