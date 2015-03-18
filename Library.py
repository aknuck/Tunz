#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from Song import *
from Playlist import *

class Library:

	playlists = []
	songs = [] #this will contain all the song objects in the library
	songList = [] #uses the user given song name. this will contain just the names of the songs for quick reference. Is in the same order as songs, so index cna be used to get song objects

	def __init__(self,directory):
		self.dir = directory
		self.songs,self.songList = self.loadSongs()
		self.playlists = self.loadPlaylists()


	#Reads all the song info in from the Song_Info.txt file and creates corresponding song objects
	#Text file lines are in the format: user given song name$file_location_name$artist name$youtube link$runtime$tag:tag:tag:tag
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
			sList.append(info[0].lower())
			s.append(Song(info[3],info[1],info[0],info[2],info[5],info[4]))
		return s,sList

	#Creates a text file containing all the songs with the info from their text files so that it can be read more quickly by the "loadSongs" method
	def createSongsInfoFile(self):
		print "edit the Song_Info.txt"

	#Creates the text file for the given song, should be used if the file has been corrupted or the song has just been added. Will overwrite the original file
	def createSongFile(self,song):
		os.chdir(song.getFilename())
		f = open("info.txt",'w')
		infoToWrite = song.getName()+"$"+song.getFilename()+"$"+song.getArtist()+"$"+song.getLink()+"$"+song.getRuntime()+"$"
		for tag in song.getTags():
			infoToWrite += tag + ":"
		infoToWrite = infoToWrite[:len(infoToWrite)-1]
		f.write(infoToWrite)
		f.close()
		os.chdir('..')
		with open('Song_Info.txt', 'a') as f:
			f.write("\n"+infoToWrite)

	#Takes in a song object and adds it to the library
	#going to replace with database entry later
	def addSong(self,song):
		self.songs.append(song)
		self.songList.append(song.getName().lower())
		self.createSongFile(song)

	def getSong(self,songName):
		if songName != None:
			if songName.lower() in self.songList:
				return self.songs[self.songList.index(songName)]
			else:
				print "[!] Song not found in library"
				return None
		return None

	def listSongs(self, arg=None): #as an arg either takes nothing (list all songs), a char (list songs starting with), or a string (list songs containing)
		sortedLib = []
		for song in self.songList:
			sortedLib.append(song)
		sortedLib.sort()
		if arg == None:
			for song in sortedLib:
				print "    - "+song.title()
		else:
			if len(arg) == 1:
				for song in sortedLib:
					if song[0] == arg:
						print "    - "+song.title()
			else:
				for song in sortedLib:
					if arg in song:
						print "    - "+song.title()

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
		match = None
		matches = [] #only to be used if there are multiple results, ideally not to be used
		for song in self.songList:
			if song.startswith(s):
				if match == None:
					match = song
				else:
					matches.append(match)
					matches.append(song)
					match = False
		if matches == []:
			return match
		else:
			print "[!] Multiple matches. Matches were:"
			for song in matches:
				print " - "+song
			return None
		

	#Checks if a song is in the library already.
	#Typ is the way to check if the song already exists, can either be "chosenName", "realName", or "youtubeLink"
	#NOTE: would like to find a better way of checking if something is already in the library, but for different purposes it needs to be able to check based on the above listed attributes
	def hasSong(self,song,typ):
		if typ == "chosenName":
			for s in self.songList:
				if song == s:
					return s
		elif typ == "fileName":
			for s in self.songs:
				if s.getFilename() == song:
					return s
		elif typ == "youtubeLink":
			for s in self.songs:
				if s.getLink == song:
					return s
		return None

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
		