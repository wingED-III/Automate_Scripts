import os
from pathlib import Path

fileName = "Touhou 6-17 characters details.txt"
filePath = "myResource/"+fileName
script_directory = os.path.dirname(__file__)
filePath = os.path.join(script_directory,filePath)

if Path(filePath).is_file():
    print ("File exist")
else:
    print ("File not exist")


file1 = open(filePath,'r',encoding="utf-8")

data = file1.read()
data = data.split("\n")

print(data)
# for line in data:
#     if line
#     print(line)






file1.close()