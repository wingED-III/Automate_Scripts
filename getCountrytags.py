import os

def strList2File(strList,fileName):
    fileTxt = open(fileName+".txt","w+")
    fileTxt.writelines(strList)
    fileTxt.close()

thisFile = __file__.replace(".","",1) #remove . at the front of str
fullPath = os.path.realpath(__file__) # reutrn  fullpath+filename
CurrentPath = fullPath.replace(thisFile,"") #get current path
#print(thisFile)
#print(CurrentPath)

items = os.listdir(os.path.join(os.path.dirname(__file__),"/myResource/countries.txt"))
print(items)
# #for i in items:
# #    i = i.replace(" - ",".")
#     #print(i.split(".")[0])
# items = list(map(lambda i:i.replace(" - ",".").split(".")[0] ,items))
# #print(items)
# for i in range(len(items)):
#         print(i,items[i])
