#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from Song import *
from Playlist import *

class Library:

	playlists = []
	songs = [] #this will contain all the song objects in the library
	songList = [] #this will contain just the names of the songs for quick reference. Is in the same order as songs, so index cna be used to get song objects

	def __init__(self,directory):
		self.dir = directory
		self.songs,self.songList = self.loadSongs()
		self.playlists = self.loadPlaylists()


	#Reads all the song info in from the Song_Info.txt file and creates corresponding song objects
	#Text file lines are in the format: user given song name$file_location_name$artist name$youtube link$tag:tag:tag:tag
	def loadSongs(self):
		s = []
		sList = []
		f = open("Song_Info.txt",'r')
		lines = f.readlines()
		for line in lines:
			info = line.split("$")
			if len(info) != 6:
				print "[!] Corrupted Song_Info file! You may want to recreate the file with the command \"restore\""
				continue
			info[len(info)-1] = info[len(info)-1].split(":")
			sList.append(info[0])
			s.append(Song(info[3],info[1],info[0],info[2],info[5],info[4]))
		return s,sList

	#Creates a text file containing all the songs with the info from their text files so that it can be read more quickly by the "loadSongs" method
	def createSongFile(self):
		print "nothing yet"

	#Takes in a song object and adds it to the library
	def addSong(self,song):


	def listSongs(self, arg=None): #as an arg either takes nothing (list all songs), a char (list songs starting with), or a string (list songs containing)
		sortedLib = []
		for song in self.songList:
			sortedLib.append(song)
		sortedLib.sort()
		if arg == None:
			for song in sortedLib:
				print "    - "+song
		else:
			if len(arg) == 1:
				for song in sortedLib:
					if song[0] == arg:
						print "    - "+song
			else:
				for song in sortedLib:
					if arg in song:
						print "    - "+song

	def listPlaylists(self, arg=None):
		if arg == None:
			for playlist in self.playlists:
				print "    - "+playlist.getName()
		else:
			if len(arg) == 1:
				for playlist in self.playlists:
					if playlist.getName()[0] == arg:
						print "    - "+playlist.getName()
			else:
				for playlist in self.playlists:
					if arg in playlist.getName():
						print "    - "+playlist.getName()

	#returns all the songs that start with the given string.
	def autocomplete(self,s):
		for song in self.songList:
			if song.startwith(s):
				

	def loadPlaylists(self):
		tempPlaylistList = []
		#try
		f = open("Tünz_Playlists.txt",'r')
		lines = f.readlines()
		for line in lines:
			info = line.split("=")
			info[1] = info[1].split(";")
			info[1][len(info[1])-1] = info[1][len(info[1])-1].split(":")
			name = info[0]
			songs = info[1][:len(info[1])-1]
			tags = info[1][len(info[1])-1]
			tempSongList = []
			for song in songs:
				tempSongList.append(self.songs[self.songList.index(song)])
			tempPlaylistList.append(Playlist(name,tempSongList,tags))
		f.close()
		return tempPlaylistList
		#CHANGE TO ERROR WITH WHOLE THING, NOT ERROR OPENING, AS THAT IS NOT THE ONLY THING THAT COULD GO WRONG
		#except:
		#	decision = ""
		#	while decision.lower() not in ('y','n'):
		#		decision = raw_input("[!] Could not find playlists file, create new one? (y/n) > ")
		#	if decision.lower() == 'y':
		#		f = open(self.dir+"Tünz_Playlists.txt",'w')
		#		f.close()
		