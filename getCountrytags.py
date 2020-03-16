import os

def strList2File(strList,fileName):
    fileTxt = open(fileName+".txt","w+")
    fileTxt.writelines(strList)
    fileTxt.close()


items = os.listdir()
#print(items)
#for i in items:
#    i = i.replace(" - ",".")
    #print(i.split(".")[0])
items = list(map(lambda i:i.replace(" - ",".").split(".")[0] ,items))
#print(items)
for i in range(len(items)):
        print(i,items[i])
