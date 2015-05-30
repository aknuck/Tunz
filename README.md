#Tünz ♫
--------
###Description

Tünz is a command line music player and downloader that makes it easy to download and play music. Downloading music is as easy as "download <song name>" and it pulls the audio from the first video in the youtube search results for that song name (There is a plan to optimize the results later to not include music videos, as those frequently have dialogue). Also acts as a music player for all the downloaded music. 

*Note: ü pronounced as it would be in german, so Tünz is pronounced Tunes ([letter ü](https://en.wikipedia.org/wiki/Ü))

Tünz.py vs Tünz2.py - Tünz2.py is the updated version that uses the other included class files. Currently unstable, but will have more features and will be easier to implement other features when done. Tünz.py is the original program with some of the commands implemented, but is somewhat stable. Can still have problems with renaming songs after downloading, resulting in "song not in your library" error, or even a crash. Not going to be fixed in Tünz.py, being fixed in Tünz2.py

-------
###Commands

**download (song)**                - downloads a song to your library

**list (songs/playlists) [start]** - Lists your songs or playlists, optionally starting with certain character(s)

**create playlist (name)**  *      - creates a playlist with given name

**add (song) :: (playlist)**  *    - adds given song in your library to given playlist

**shuffle [playlist]**  *          - shuffles your main library or a specific playlist

**play (song/playlist)**           - plays the current music if no argument give, or plays a song or a playlist

**queue manual/auto***             - changes the way songs queue. If on manual, use "q" command to add to the queue

**q

**delete (song/playlist)**  *      - removes a song or a playlist

**pause**                          - pauses the music

**rewind**   *                     - rewinds the music

**skip**  *                        - skips to the next song

**info**                           - gives info about Tünz

**exit**                           - exits Tünz

*Command still needs to be added
NOTE - to queue songs in Tünz.py "add" command is used to queue songs when set to auto. Some other commands may not exist yet

-------
###Dependencies

Pygame

youtube-dl

-------
###To Be Added

*In the middle of adding playlists and properly adding songs to Tünz2.py
*Lyrics to be pulled from the internet when possible
*Add commands to play or sort songs by their tags
*Autocomplete song names if there is only one with the given name
*More advanced search to search starting with a certain string, containing a certain string, having certain tags, artists, lyrics, or links
*commands noted as still need to be added above
