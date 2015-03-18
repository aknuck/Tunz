#!/usr/bin/env python
# -*- coding: utf-8 -*-

#A class to store the info on playlists
class Playlist:

	def __init__(self,name,songs=[],tags=[]):
		self.name = name
		self.songs = songs
		self.tags = tags

	def getName(self):
		return self.name

	#takes a song object as parameter, adds to the playlist's list of songs
	def addSong(self,song):
		self.songs.append(song)

	def getSongs(self):
		return self.songs

	def getSongNames(self):
		names = []
		for song in self.songs:
			names.append(song.getName())
		return names