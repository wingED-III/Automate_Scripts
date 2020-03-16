import os

fileName = "Touhou 6-17 characters details.txt"
filePath = "myResource/"+fileName
script_directory = os.path.dirname(__file__)
filePath = os.path.join(script_directory,filePath)

file1 = open(filePath,'r')
