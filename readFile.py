import os
from pathlib import Path
import pandas as pd



fileName = "Touhou 6-17 characters details.txt"
outputFile = "Touhou characterName"

filePath = "myResource/"+fileName
script_directory = os.path.dirname(__file__)
filePath = os.path.join(script_directory,filePath)

if Path(filePath).is_file():
    print ("File exist")
else:
    print ("File not exist")



file1 = open(filePath,'r',encoding="utf-8")

data = file1.read()

file1.close()

data = data.split("\n")

#print(data)
prev = data[0]
i = 0
characterNameList = []

for line in data:

    if "Species" in line:
        i+=1
        nameLine = prev.split()
        firstname,surname = nameLine[0],nameLine[1]
        fullName = firstname+" "+surname
        characterNameList.append(fullName)
        #print("{}  {}".format(i,fullName))

    prev = line

#print(characterNameList)

df = pd.DataFrame(characterNameList)
#print(df)
df.to_csv(outputFile+'.csv')