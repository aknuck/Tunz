#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tünz
#Adam Knuckey February 2015

#TODO
#Add multithreading to support queueing and checking when song ends. needed for playlists
#create Song class and use that instead of current system. Will make it easier to sort and play songs, can more easily shuffle
#rename songs
#categorize songs (eg list songs rock would show all songs that you've given the attribute 'rock' to)
#add artists to songs (eg list songs by (artist) will show all the songs that you've said are by that artist)
#info (song) will show complete info on characteristics you've given it (ie title, artist, attributes)
#auto complete (eg type in just the first word of the title and if there are no other ones with that starting word it will know to play that song)
#going to need to make a text file to store the information given on the songs so it can be loaded in later instances of the program
#for downloading split at commas and download each of the ones in the list to streamline downloading
#relevant to one above - clean inputs so there are no commas or other special characters
#figure out how to download to a specific directory with youtube-dl
#when saving playlist or song information to a file, save it to a temp file and then rename the temp file while deleting the old one just so if it crashes part way through, it still there in the original. Add a character at the end of the file like a & or $ to show that the operation completed so when reading it doesnt read from an incomplete file
#pull song info from online dataabases, such as release year and lyrics. lyrics would be cool to have only a couple of words away
#when renaming a song make sure there isn't a song by that name left
#pull song length from the youtube video
#add command "song info (song)" or something like it that prints information on the song
#add feature of queue that when no argument is given with it it prints out songs that are queued
#add command to deque a song

print "Starting Tünz..."
import os
import sys
import datetime
import urllib2
import threading
from pygame import mixer

from Library import *
from MusicPlayer import *
from Playlist import *
from Song import *

mixer.init()


class Tunz:

    def __init__(self):
        self.dir = os.getcwd()
        self.library = Library(self.dir)
        self.musicPlayer = MusicPlayer(self.library)


    #A method to change directories to the main Tünz directory. It will first check if it is in that directory, and if it's not it cds into it
    def mainDir(self):
        print ""+os.getcwd()
        print self.dir
        if os.cwdir() == self.dir:
            print "in directory"
        else:
            print "changing"
            os.chdir('..')

    #A method to change directories to the Tünz Library directory. It will first check if it is in that directory, and if it's not it cds into it
    def libDir(self):
        print ""+os.getcwd()
        print self.dir
        if os.getcwd() != self.dir:
            print "in directory"
        else:
            print "changing"
            os.chdir('Tünz Library')

    #loads all the songs in your library into an array to be used for playing the songs and displaying them
    def updateLibrary(self):
        self.library = []
        for song in next(os.walk('.'))[1]:
            self.library.append(song)
        self.library.sort()

    def queueSongs(self):
        i = self.library.index(self.currentSong)
        for song in self.library[i:]:
            mixer.music.queue(song+"/"+song+".mp3")

    def queueSong(self,song):
        mixer.music.queue(song+"/"+song+".mp3")

    #download a song based by the name given in the command
    def download(self,command):
        #NOTE check input
        currentDL = Download(command)
        self.library.addSong(currentDL.getSong())

    def goto(self,command):
        if len(command) == 2:
            if self.playing:
                mixer.music.play(0,(int(command[1])))
            else:
                print "[x] Nothing playing!"
        else:
            print "[x] format of 'goto' is goto (time)"

    def play(self,command):
        if len(command) == 1:
            if self.currentSong == "No Song Selected":
                print ("[x] "+self.currentSong)
            else:
                mixer.music.unpause()
                self.playing = True
        else:
            command.remove(command[0])
            command = "_".join(command)
            if command in self.library:
                #try:
                mixer.music.load(command+"/"+command+".mp3")
                self.currentSong = command
                mixer.music.play()
                self.playing = True
                if not self.manualQueue:
                    self.queueSongs()
                #except:
            else:
                print "[x] Song isn't in your library"

    def add(self,command):
        if self.manualQueue:
            if len(command) == 1:
                print ("[x] Syntax for add - 'add (song)")
            else:
                command.remove(command[0])
                command = "_".join(command)
                if command in self.library:
                    #try:
                    #mixer.music.load(command+"/"+command+".mp3")
                    self.queueSong(command)
                    print "[+] Song queued!"
                    #except:
                else:
                    print "[x] Song isn't in your library"
        else:
            print "[x] manual queue is not on. Use 'queue manual' to switch"

    def stop(self):
                mixer.music.stop()
                self.playing = False
                self.currentSong = "No Song Selected"

    def list(self,command):
        if len(command) == 2:
            if command[1] == "songs":
                self.library.listSongs()
            elif command[1] == "playlists":
                self.library.listPlaylists()
            else:
                print "[x] format for 'list' - list (song/playlist) [start/contains]"
        elif len(command) == 3 and len(command[2]) == 1:
            if command[1] == "songs":
                self.library.listSongs(command[2])
            elif command[1] == "playlists":
                self.library.listPlaylists(command[2])
            else:
                print "[x] format for 'list' - list (song/playlist) [start/contains]"
        elif len(command) >= 3:
            if command[1] == "songs":
                self.library.listSongs(" ".join(command[2:len(command)]))
            elif command[1] == "playlists":
                self.library.listPlaylists(" ".join(command[2:len(command)]))
            else:
                print "[x] format for 'list' - list (song/playlist) [start/contains]"
        else:
            print "[x] format for 'list' - list (song/playlist) [start/contains]"


    def start(self):
        while True:
            command = raw_input("[♫] ").split(" ")

            if command[0] == "help": #HELP -----------
                print self.commandList

            elif command[0] == "download": #DOWNLOAD -----------
                self.download(command)

            elif command[0] == "list": #LIST ----------
                self.list(command)

            elif command[0] == "add":
                self.add(command)

            elif command[0] == "goto":
                self.goto(command)

            elif command[0] == "play":
                self.play(command)

            elif command[0] == "pause":
                mixer.music.pause()
                self.playing = False

            elif command[0] == "stop":
                self.stop()

            elif command[0] == "queue":
                if len(command) == 2:
                    if command[1] == "manual":
                        self.stop()
                        self.manualQueue = True
                        print "[+] Now on manual queue"
                    elif command[0] == "auto":
                        self.stop()
                        self.manualQueue = False
                        print "[+] Now on auto queue"
                    else:
                        print "[x] format for queue - 'queue (manual/auto)'"
                else:
                    print "[x] format for queue - 'queue (manual/auto)'"

            elif command[0] == "current":
                if len(command) == 1:
                    if self.currentSong != "No Song Selected":
                        print "[+] Current Song is "+self.currentSong.replace("_"," ")+" ("+str(datetime.timedelta(seconds=mixer.music.get_pos()/1000))+")"
                    else:
                        print "[x]"+self.currentSong
                elif len(command) == 2 and command[1] == "playlist":
                    if self.currentPlaylist != "No Playlist Selected":
                        print "[+] Current playlist is "+self.currentPlaylist
                    else:
                        print "[x] No Playlist Selected"

            elif command[0] == "exit" or command[0] == "quit": #EXIT -----------
                sys.exit(0)    

if __name__ == "__main__":
    os.system("\nmkdir \"Tünz Library\"")
    os.chdir("Tünz Library")
    print "path is "+os.getcwd()+"\n" 
    print "---------------Tünz--------------"
    print "    Command Line Music Player    "
    print "         By Adam Knuckey         "
    print "---------------------------------"
    #open("Tünz_Playlists.txt",'w').close()
    print "\n Type 'help' for a list of commands"
    tunz = Tunz()
    tunz.start()