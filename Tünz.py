#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Tünz
#Adam Knuckey February 2015

print "Starting Tünz..."
import os
import sys
import datetime
import urllib2
from pygame import mixer
mixer.init()

class Tunz:

    def __init__(self):
        os.system("mkdir \"Tünz Library\"")
        self.currentSong = "No Song Selected"
        self.currentPLaylist = "No Playlist Selected"
        self.library = []
        self.playing = False #can also use mixer.music.get_busy()
        commandList = "download (song) - downloads a song to your library \nlist (songs/playlists) [start] - Lists your songs or playlists, optionally starting with certain character(s) \ncreate playlist (name) - creates a playlist with given name \nadd (song) :: (playlist) - adds given song in your library to given playlist \nshuffle [playlist] - shuffles your main library or a specific playlist \nplay (song/playlist) - plays the current music if no argument give, or plays a song or a playlist \ndelete (song/playlist) - removes a song or a playlist \npause - pauses the music \nrewind - rewinds the music \nskip - skips to the next song\ninfo - gives info about Tünz \nexit - exits Tünz"
        self.updateLibrary()

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

    #download a song based by the name given in the command
    def download(self,command):
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
            try:
                mixer.music.load(command+"/"+command+".mp3")
                self.currentSong = command
                mixer.music.play()
                self.playing = True
                self.queueSongs()
            except:
                print "[x] Song isn't in your library"

    def start(self):
        while True:
            command = raw_input("[♫] ").split(" ")

            if command[0] == "help": #HELP -----------
                print commandList

            elif command[0] == "download": #DOWNLOAD -----------
                self.download(command)

            elif command[0] == "list": #LIST ----------
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
            elif command[0] == "goto":
                self.goto(command)

            elif command[0] == "play":
                self.play(command)

            elif command[0] == "pause":
                mixer.music.pause()
                self.playing = False

            elif command[0] == "stop":
                mixer.music.stop()
                self.playing = False
                self.currentSong = "No Song Selected"

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
    os.chdir("Tünz Library")
    open("Tünz_Playlists.txt",'w').close()
    print "path is "+os.getcwd()+"\n" 
    print "\n Type 'help' for a list of commands"
    tunz = Tunz()
    tunz.start()