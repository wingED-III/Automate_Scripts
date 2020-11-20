import os

nameList = None
name_path = 'myResource/touhou Changeability of Strange Dream namelist.txt'
folder_path = 'myResource/touhou Changeability of Strange Dream'

# print(os.listdir('myResource'))
# os.getcwd()

with open(name_path,'r') as f:
   nameList=  f.read().split('\n')

# name_pattern = "1331170_x_1.mp3"
ext = ".mp3"
for i in range(1,12):
    name_pattern = "1331170_1_x"+ext
    name_pattern =  name_pattern.replace('x',str(i))
    new_name = "ZUN's Collection 3_"+str(i)+" "+nameList[i-1]+ext
    print(name_pattern.ljust(20,' '),'->',new_name)
    os.rename(folder_path+"/"+name_pattern,folder_path+"/"+new_name)
