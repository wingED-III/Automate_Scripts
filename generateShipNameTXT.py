import os
import pandas as pd

class THgame:
    def __init__(self,number,name,abrv):
        self.number = number
        self.numberStr = str(number)
        self.name = name
        self.abrv = abrv
    
    def __str__(self):
        return str(self.number)+","+self.name+","+self.abrv

def main():
    # filePath ='output/Touhou first Name Only v1.csv'
    # characterDF = pd.read_csv(filePath)
    # print(characterDF.head())
 
    filePath ='myResource/touhou_game_names.csv'
    gameDF = pd.read_csv(filePath)
    #print(gameDF.head())


    gameList=[]
    gameDF = gameDF.values.tolist()
    #print(gameDF)
    for game in gameDF:
            gameList.append(THgame(game[0],game[1],game[2]))

    # for game in gameList:
    #     print(game)

    nameList = "--------"
    genrateStr(gameList[0],nameList)

    pass


def genrateStr(thgame=THgame,nameList =""):
    strTemplate = "#th"+thgame.numberStr+"\n"
    strTemplate += "TOUHOU_"+thgame.abrv+"_NAME"+" = {\n"
    name_in_localisation = "NAME_TOUHOU_"+thgame.abrv
    strTemplate += name_in_localisation+"/n/n"
    strTemplate += "type = ship\n\n"
    strTemplate += 'fallback_name = "Touhou '+thgame.abrv+" %"+'d"\n'
    strTemplate += "unique = {\n"
    strTemplate += nameList
   

    strTemplate+="\n }\n}"
    print(strTemplate)
    pass
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

if __name__ == "__main__":
    main()

