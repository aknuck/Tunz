#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Song import *
from Library import *
from threading import Thread
import datetime
from pygame import mixer
from pygame import time
#from pygame import *


#A class to be run in another thread to play the music
#Because of the way PyGame does queueing and checking if song ends, it needs to be running in another thread
#It will loop to check if the current song ended to as to queue the next appropriate song (only one song can be queued at a time)
class MusicPlayer(Thread):

	def __init__(self,lib,qMode=True):
		Thread.__init__(self)
		self.library = lib
		self.manualQueueMode = qMode #either True (manual queue) or False (auto queue)
		self.currentSong = None
		self.playing = False
		self.running = True
		self.queue = []
		self.queuePos = 0
		self.songTime = 0
		self.clock = time.Clock()
		mixer.init()

	#invoked when started as a new thread. Will contain the main loop of this thread, checking if a song is over and queueing etc
	def run(self):
		print ""
		while self.running:
			if self.playing:
				if mixer.music.get_busy():
					self.clock.tick(30)
				else:
					if self.playing:
						self.queuePos += 1
						if self.queuePos < len(self.queue):
							self.play(self.queue[self.queuePos].getName())
			self.clock.tick(30)

	def exit(self):
		self.stop()
		self.running = False

	def play(self,command):
		if len(command) == 1:
			if self.currentSong == None:
				if self.queuePos < len(self.queue):
					currentSong = self.queue[self.queuePos]
					self.playing = True
					mixer.music.load(currentSong.getFilename()+"/"+currentSong.getFilename()+".mp3")
					mixer.music.play()

				print ("[x] No song selected!")
			else:
				self.unpause()
		else:
			command.remove(command[0])
			command = " ".join(command)
			song = self.library.getSong(self.library.autocomplete(command))
			if song != None:
				self.playing = True
				mixer.music.load(song.getFilename()+"/"+song.getFilename()+".mp3")
				self.currentSong = song
				mixer.music.play()

	def queue(self,song):
		self.queue.append(song)
	
	def currentSong(self):
		print self.currentSong.getName()
		return self.currentSong

	def pause(self):
		if self.playing:
			mixer.music.pause()
			self.playing = False

	def unpause(self):
		if not self.playing:
			mixer.music.unpause()

	def stop(self):
		mixer.music.stop()
		self.playing = False
		self.running = False
		self.currentSong = None

	def queue(self,song):
		print ""

