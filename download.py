#download class

class download:

	def __init__(self,command):

		self.downloadName = " ".split(command)[1:].join() #gets the song name from the command
		print "[+] downloading "+self.downloadName
		self.link = ""
		self.runtime = ""
		downloadSong(self.downloadName)
		print "[!] finished downloading\n"
		print "enter attributes. leave blank for default"
		self.givenName = raw_input("Name: ")
		self.artist = raw_input("Artist: ")

	def downloadSong(self, name):
		if name != "":
			
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