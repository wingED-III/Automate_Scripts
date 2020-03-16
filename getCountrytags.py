import os
import glob

def strList2File(strList,fileName):
    fileTxt = open(fileName+".txt","w+")
    fileTxt.writelines(strList)
    fileTxt.close()


outputFile = "hoi4_all_country_tags"
pathContainFiles = "\myResource\countries"
thisFile = __file__.replace(".","",1) #remove . at the front of str
fullPath = os.path.realpath(__file__) # reutrn  fullpath+filename
CurrentPath = fullPath.replace(thisFile,"") #get current path
#print(thisFile)
#print(CurrentPath)
targetPath = CurrentPath+pathContainFiles

items = os.listdir(targetPath)
#print(items)
seperator = ","
items = list(map(lambda i:i.replace(" - ",".").split(".")[0]+seperator ,items)) # extract tags from file name
#print(items)

strList2File(items,outputFile)

