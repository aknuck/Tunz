#Tünz
--------
###Description

Tünz is a command line music player and downloader. To get music you type in "download <song name>" and it pulls the audio from the first video in the youtube search results for that song name (There is a plan to optimize the results later to not include music videos, as those frequently have dialogue).

-------
###Commands

**download (song)**                - downloads a song to your library

**list (songs/playlists) [start]** - Lists your songs or playlists, optionally starting with certain character(s)

**create playlist (name)**         - creates a playlist with given name

**add (song) :: (playlist)**       - adds given song in your library to given playlist

**shuffle [playlist]**             - shuffles your main library or a specific playlist

**play (song/playlist)**           - plays the current music if no argument give, or plays a song or a playlist

**delete (song/playlist)**         - removes a song or a playlist

**pause**                          - pauses the music

**rewind**                         - rewinds the music

**skip**                           - skips to the next song

**info**                           - gives info about Tünz

**exit**                           - exits Tünz


-------
###Dependencies

Pygame
youtube-dl

-------
###To Be Added

Playlsits still need to be added, and the music player is going to be moved to anther thread for more functionality

