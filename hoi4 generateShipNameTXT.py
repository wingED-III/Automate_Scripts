import os
import pandas as pd
import math

class THgame:
    def __init__(self,number,name,abrv):
        self.number = number
        self.numberStr = str(number)
        self.name = name
        self.abrv = abrv
        self.characterList = []
        self.localName = "NAME_TOUHOU_"+abrv # for localisation file
    
    def __str__(self):
        return str(self.number)+","+self.name+","+self.abrv+ ",["+",".join(self.characterList)+"]"

def main():
    outputFile = 'Touhou_ship_names'
    localisationFile = "TouhouShipName"
    filePath ='myResource/Touhou first Name Only v2.csv'
    characterDF = pd.read_csv(filePath)
    #print(characterDF.head())
 
    filePath ='myResource/touhou_game_names v2.csv'
    gameDF = pd.read_csv(filePath)
    #print(gameDF.head())

    gameList=[]
    gameDF = gameDF.values.tolist()
    #print(gameDF)
    for game in gameDF:
            gameList.append(THgame(game[0],game[1],game[2]))

    # for game in gameList:
    #     print(game)

    characterDF = characterDF[['Name','first_appearance']]
    #print(characterDF.head())
    characterList = characterDF.values.tolist()
    # for x in characterList:
    #     print(x)
    #print(characterList)

    sortCharacter2GameList(characterList,gameList)
    
    # for game in gameList:
    #     print(game)

    printList = []
    for game in gameList:
        if len(game.characterList) > 0:
            printList.append(generateNamePatterns(game,game.characterList))


    strList2File(printList,fileName=outputFile)

    ## Generate Shipname.yml ##
    generateLocalisationPattern(fileName=localisationFile,thgameList=gameList)

    pass

def generateLocalisationPattern(fileName,thgameList=[]):
### pattern
    #  l_english:
    #  NAME_THEME_PREFECTURES:0 "Provinces & Prefectures"
    strTemplate = "l_english:"+"\n"
    for game in thgameList:
        strTemplate+= game.localName+":0 "+"\"Touhou "+game.name +"\"\n"
        
    strList2File(strTemplate,fileName=fileName+"_l_english.yml")
    pass

def sortCharacter2GameList(nameList,thgameList):
    round = 0
    for item in nameList:
        appearNumber = item[1];
        if math.isnan(appearNumber):
            continue;

        for game in thgameList:
            if appearNumber == game.number:
                # print(item[0],appearNumber,game.number)
                game.characterList.append(item[0])
                round = round+1
                break;
    print("Number of character =",round)
    pass

def generateNamePatterns(thgame=THgame,nameList =[]):
        ### generate
    # #th6
    # TOUHOU_EOSD_NAME = {
    # 	name = NAME_TOUHOU_EOSD

    # 	type = ship

    # 	fallback_name = "Touhou EOSD %d"
    # 	unique = {
    # 		"Rumia" "Daiyousei" "Cirno" "Meiling" "Koakuma" "Patchouli" "Sakuya" "Remilia" 
    # 		"Flandre" 
    # 	}
    # }
    strTemplate = "#th"+thgame.numberStr+"\n"
    strTemplate += "TOUHOU_"+thgame.abrv+"_NAME"+" = {\n"
    name_in_localisation = "\tname = "+thgame.localName +"\n\n"
    strTemplate += "\ttype = ship\n\n"
    strTemplate += '\tfallback_name = "Touhou '+thgame.abrv+" %"+'d"\n'
    strTemplate += "\tunique = {\n"

    nameListStr ="\t\t"
    count = 0
    for name in nameList:
        nameListStr += '"'+name+'" '
        count += 1
        if count == 10:
            count = 0
            nameListStr+="\n\t\t"        

    strTemplate += nameListStr

    strTemplate+="\n\t}\n}\n\n"
    #print(strTemplate)
    return strTemplate
    pass


def strList2File(strList,fileName):
    fileTxt = open(fileName+".txt","w+")
    fileTxt.writelines(strList)
    fileTxt.close()


if __name__ == "__main__":
    main()

