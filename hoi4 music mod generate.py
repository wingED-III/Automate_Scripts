import os

def createMusicTXT(musicList,playlistName):
    musicTxt = open(playlistName+"_song.txt","w+")

    musicTxt.write("music_station = "+playlistName+"\n\n")
    musicList = map(lambda fileX:code_for_a_song(fileX) ,musicList)
    musicTxt.writelines(musicList)
    musicTxt.close()

def formatFilename(fileName):
    charToReplace = "- +"
    for i in range(len(fileName)):
        if fileName[i] in charToReplace:
            fileName = fileName.replace(fileName[i],"_")
            #print(fileName[i]+":",fileName)
    fileName = fileName[:-4].lower()+"\n" # exclude extension 
    return fileName 

def code_for_a_song(fileName):
    fileName = formatFilename(fileName)
    return "music ={\n\t"+fileName+"\n}\n\n" 
    
#create str below    
#music = {
# 	song = "songName"
#}   


extensionTarget = ".ogg"
items = os.listdir()
#print(items)
musicOgglist = filter(lambda fileX:extensionTarget == os.path.splitext(fileX)[1]  ,items) # os.path.splitext(fileX)[1] # 0 is a file name.
musicOgglist = list(musicOgglist)
playlistName = input("Enter playlist name [No spacebar,only english lowercase alphabet]:\n")
createMusicTXT(musicOgglist,playlistName)
