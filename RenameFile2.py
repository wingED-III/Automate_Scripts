import os
from datetime import datetime


def my_rename(path, old, new):
    os.rename(path+"/"+old, folder_path+"/"+new)


def print_compare(old, new):
    print(old.ljust(20, ' '), '->', new)


nameList = None
folder_path = 'myResource/for_renaming'

# print(os.listdir(folder_path))

# old_name_pattern = "reddit_submission_{}_{}.csv"
# new_name_pattern = "reddit_touhou_submissions_{}_{}.csv"

ext = ".csv"
# year = 2020
# for i in range(1, 8):
#    just_date = datetime(year, i, 1)
#    old_name = old_name_pattern.format(just_date.strftime('%B'), just_date.year)
#    new_name = new_name_pattern.format(just_date.year, just_date.strftime('%B'))
#    print(old_name.ljust(20, ' '), '->', new_name)

#      #rename
#    os.rename(folder_path+"/"+old_name,folder_path+"/"+new_name)

# swap words
nameList = os.listdir(folder_path)

for name in nameList:
    word_array = name.replace(ext, '').split('_')
   #  print(word_array)
    new_name = ''
    for i in [0, 1, 2, 4, 3]:
        new_name = new_name + word_array[i] + '_'

    new_name = new_name[:-1] + ext
    print_compare(name, new_name)
    my_rename(folder_path, name, new_name)
