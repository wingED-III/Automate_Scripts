import os
from pathlib import Path
import pandas as pd


def main():
    fileName = "Touhou others characters details.txt"
    outputFile = fileName[:-4]+" Name Only"

    filePath = "myResource/"+fileName
    script_directory = os.path.dirname(__file__)
    filePath = os.path.join(script_directory,filePath)

    if Path(filePath).is_file():
        print (fileName+":File exist")
    else:
        print (fileName+":File not exist")
        return


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
            #characterNameList.append(fullName)
            #print("{}  {}".format(i,fullName))

            characterNameList.append(firstname)
            
        prev = line

    #print(characterNameList)

    # Write to csv
    df = pd.DataFrame(characterNameList,columns=['Name'])
    #print(df)
    df.to_csv(outputFile+'.csv')

if __name__ == "__main__":
    main()