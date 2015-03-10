#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Class to store information on songs including filename
class Song:

    #Takes String name, String artist, and Array<String> attributes
    #filename is taken from the download and is the name of the file and folder in the library. Used to load the song
    #When the song is requested to be downloaded from the Tunz class, it should ask for these things that need to be passed
    #keep entering attributes until blank
    #to get song length search for </div><span class="video-time" aria-hidden="true"> and length is right afterwards. be carefule of hour long songs, as it changes from X:XX to X:XX:XX
    def __init__(self,link,filename,name,artist,tags,runtime):
        self.link = link #link to the YouTube video of the song
        self.filename = filename #name of the file stored in the library
        self.name = name.capitalize() #song artist
        self.artist = artist #Song artist
        self.tags = tags #A list of attributes of the song, such as "rock, alternative"
        self.runtime = runtime

    def getRuntime(self):
        return self.runtime

    def getLink(self):
        return self.link

    def getFilename(self):
        return self.filename

    def getName(self):
        return self.name

    def getArtist(self):
        return self.artist

    def getTags(self):
        return self.tags


