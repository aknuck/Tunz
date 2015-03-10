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

print "Starting Tünz..."
import os
import sys
import datetime
import urllib2
import threading
from pygame import mixer
mixer.init()


#Class to store information on songs including filename
class Song:

    #Takes String name, String artist, and Array<String> attributes
    #filename is taken from the download and is the name of the file and folder in the library. Used to load the song
    #When the song is requested to be downloaded from the Tunz class, it should ask for these things that need to be passed
    #keep entering attributes until blank
    #to get song length search for </div><span class="video-time" aria-hidden="true"> and length is right afterwards. be carefule of hour long songs, as it changes from X:XX to X:XX:XX
    def __init__(self,link,filename,name,artist,attributes):
        self.link = link #link to the YouTube video of the song
        self.filename = filename #name of the file stored in the library
        self.name = name #song artist
        self.artist = artist #Song artist
        self.attributes = attributes #A list of attributes of the song, such as "rock, alternative"

    def getLink():
        return self.link

    def getFilename():
        return this.filename

    def getName():
        return this.name

    def getArtist():
        return this.artist

    def getAttributes():
        return this.attributes

#A class to store the info on playlists
class Playlist:

    def __init__(self,name):
        self.name = name
        self.songs = []
        self.tags = []

    #takes a song object as parameter, adds to the playlist's list of songs
    def addSong(self,song):
        self.songs.append(song)

    def getSongs(self):
        return self.songs

    def getSongNames(self):
        names = []
        for song in songs:
            names.append(song.getName())
        return names


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

class Library:

    playlists = []
    songs = []

    def __init__(self,directory):
        self.dir = directory

    def loadPlaylists(self):
        print ""


##----THIS CLASS HAS BEEN PUT ON HOLD BECAUSE IT CANT DOWNLOAD TO THE RIGHT LOCATION IF MUSIC IS BEING CHOSEN AS THEY USE THE SAME LOCATION-----##
#Used to download songs in the background(another thread) so user can run commands while a song is downloading
#That's basically it
#class Downloader:#

#    def __init__(self,library):
#        self.library = library #NOTE will have to change how this is handled when song objects are implemented#

#    #Is passed the name of the YouTube video to be downloaded in the form of the user command
#    #Downloads the image and mp3 from the first YouTube video assosciated with that title in a YouTube search
#    def download(self,command,parent):
#        print os.getcwd()
#        if len(command) >= 1:
#            song = ""
#            if len(command) == 1:
#                while song == "":
#                    song = raw_input("\n > Enter a song to download: ").replace(" ","_")
#            else:
#                command.remove(command[0])
#                song = " ".join(command).replace(" ","_")
#            answer = 'y'
#            if song in self.library:
#                print "[!] Song is already in your library! Do you want to replace it? (y/n)"
#                answer = ""
#                while answer.lower() not in ['y','n']:
#                    answer = raw_input("   > ")
#            if answer.lower() == 'y':
#                os.system("mkdir \""+song+"\"")
#                songTitle = song.split(" ")
#                os.chdir(song)
#                baseLink = "https://www.youtube.com/results?search_query="
#                for word in songTitle:
#                    baseLink = baseLink + word + "+"
#                baseLink = baseLink[:len(baseLink)-1]
#                baseLink = baseLink + "&page=&utm_source=opensearch"
#                page = urllib2.urlopen(baseLink)
#                html = page.read()
#                youtubeLink = "https://www.youtube.com/watch?v="+html[html.index("/watch?v=")+9:html.index("/watch?v=")+20]
#                print "\nfound "+youtubeLink
#                print "[+] Downloading, please wait..."
#                print "[+] Downloading Image..."
#                os.system("wget -q -nd -r -P "+os.getcwd()+" -A jpeg,jpg,bmp,gif,png https://i.ytimg.com/vi/"+html[html.index("/watch?v=")+9:html.index("/watch?v=")+20]+"/mqdefault.jpg --no-check-certificate")
#                print "[+] Downloading MP3...\n"
#                #os.chdir('..')
#                #os.system("youtube-dl -t --write-thumbnail -q "+youtubeLink+" --extract-audio --audio-format mp3")
#                #print "\""+os.getcwd()+"/"+song+"\""
#                os.system("youtube-dl -t --write-thumbnail -q "+youtubeLink+" --extract-audio --audio-format mp3")#

#                if ".mp3" in next(os.walk('.'))[2][1]:
#                    os.system("mv \""+next(os.walk('.'))[2][1]+"\" "+song+".mp3")
#                    os.system("mv \""+next(os.walk('.'))[2][0]+"\" "+song+".jpg")
#                else:
#                    os.system("mv \""+next(os.walk('.'))[2][0]+"\" "+song+".mp3")
#                    os.system("mv \""+next(os.walk('.'))[2][1]+"\" "+song+".jpg")
#                print "[+] DONE!\n"
#                parent.libDir()
#                parent.updateLibrary()
#        else:
#            print "[x] Format for 'download' - download (song)"#


class Tunz:

    def __init__(self):
        self.dir = os.getcwd()
        self.currentSong = "No Song Selected"
        self.currentPLaylist = "No Playlist Selected"
        self.manualQueue = True
        self.library = []
        self.playing = False #can also use mixer.music.get_busy()
        self.commandList = "download (song) - downloads a song to your library \nlist (songs/playlists) [start] - Lists your songs or playlists, optionally starting with certain character(s) \ncreate playlist (name) - creates a playlist with given name \nadd (song) :: (playlist) - adds given song in your library to given playlist \nshuffle [playlist] - shuffles your main library or a specific playlist \nplay (song/playlist) - plays the current music if no argument give, or plays a song or a playlist \ndelete (song/playlist) - removes a song or a playlist \npause - pauses the music \nrewind - rewinds the music \nskip - skips to the next song\ninfo - gives info about Tünz \nexit - exits Tünz"
        self.updateLibrary()
        #self.downloader = Downloader(self.library)

#    def __init__(self):
#        self.dir = os.getcwd()
#        self.library = Library(self.dir)
#        self.musicPlayer = MusicPlayer(self.library)


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
        #t = threading.Thread(target=Downloader.download, args = (self.downloader,command,self))
        #t.start()
        if len(command) >= 1:
            song = ""
            if len(command) == 1:
                while song == "":
                    song = raw_input("\n > Enter a song to download: ").replace(" ","_")
            else:
                command.remove(command[0])
                song = " ".join(command).replace(" ","_")
            answer = 'y'
            if song in self.library:
                print "[!] Song is already in your library! Do you want to replace it? (y/n)"
                answer = ""
                while answer.lower() not in ['y','n']:
                    answer = raw_input("   > ")
            if answer.lower() == 'y':
                os.system("mkdir \""+song+"\"")
                songTitle = song.split(" ")
                os.chdir(song)
                baseLink = "https://www.youtube.com/results?search_query="
                for word in songTitle:
                    baseLink = baseLink + word + "+"
                baseLink = baseLink[:len(baseLink)-1]
                baseLink = baseLink + "&page=&utm_source=opensearch"
                page = urllib2.urlopen(baseLink)
                html = page.read()
                youtubeLink = "https://www.youtube.com/watch?v="+html[html.index("/watch?v=")+9:html.index("/watch?v=")+20]
                print "\nfound "+youtubeLink
                print "[+] Downloading, please wait..."
                print "[+] Downloading Image..."
                os.system("wget -q -nd -r -P "+os.getcwd()+" -A jpeg,jpg,bmp,gif,png https://i.ytimg.com/vi/"+html[html.index("/watch?v=")+9:html.index("/watch?v=")+20]+"/mqdefault.jpg --no-check-certificate")
                print "[+] Downloading MP3..."
                os.system("youtube-dl -t --write-thumbnail -q "+youtubeLink+" --extract-audio --audio-format mp3")
                #os.system("youtube-dl  --extract-audio --audio-format mp3 -o "+self.dir+"/\\Tünz \\Library/"+song+" -q "+youtubeLink)
                print os.getcwd()
                if ".mp3" in next(os.walk('.'))[2][1]:
                    os.system("mv \""+next(os.walk('.'))[2][1]+"\" "+song+".mp3")
                    os.system("mv \""+next(os.walk('.'))[2][0]+"\" "+song+".jpg")
                else:
                    os.system("mv \""+next(os.walk('.'))[2][0]+"\" "+song+".mp3")
                    os.system("mv \""+next(os.walk('.'))[2][1]+"\" "+song+".jpg")
                print "[+] DONE!\n"
                os.chdir('..')
                self.updateLibrary()
        else:
            print "[x] Format for 'download' - download (song)"

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

    def start(self):
        while True:
            command = raw_input("[♫] ").split(" ")

            if command[0] == "help": #HELP -----------
                print self.commandList

            elif command[0] == "download": #DOWNLOAD -----------
                self.download(command)

            elif command[0] == "list": #LIST ----------
                self.updateLibrary()
                if len(command) >= 2:
                    start = "" #If the user wants to list only those songs or playlists starting with a certain string
                    if len(command) > 2:
                        start = " ".join(command[2:])
                    if command[1] == "songs":
                        if len(command) > 2:
                            print "songs starting with "+start+":"
                        for song in next(os.walk('.'))[1]:
                            if song.replace("_"," ").startswith(start):
                                print "   - "+song.replace("_"," ")+"\n" 
                    elif command[1] == "playlists":
                        if len(command) > 2:
                            print "playlists starting with "+start+":"
                        with open("Tünz_Playlists.txt",'r') as f:
                            for line in f:
                                if line.startswith(start):
                                    print line
                    else:
                        print "[x] format for 'list' - list (song/playlist) [start]"
                else:
                    print "[x] format for 'list' - list (song/playlist) [start]"

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
    print "---------------Tünz--------------"
    print "    Command Line Music Player    "
    print "         By Adam Knuckey         "
    print "---------------------------------"
    os.system("mkdir \"Tünz Library\"")
    os.chdir("Tünz Library")
    open("Tünz_Playlists.txt",'w').close()
    print "path is "+os.getcwd()+"\n" 
    print "\n Type 'help' for a list of commands"
    tunz = Tunz()
    tunz.start()