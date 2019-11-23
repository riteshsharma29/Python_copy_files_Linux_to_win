#!/usr/bin/python3

import os

os.chdir("/var/log")
c_dir = os.getcwd()

main_list = []

def loop_into_folders(path):
    items = os.listdir(path)
    for item in items:
        os.chdir(path)
        if os.path.isdir(item):
            loop_into_folders(os.path.join(path,str(item)))
        else:
            if str(item).endswith('log'):
                main_list.append([item,os.stat(item).st_size],)
    pass 
    #print(main_list)                

loop_into_folders("/var/log")

duplicate = []
size = 0



for x in main_list:
    if main_list.count(x) > 1:
        duplicate.append(x)
        size += x[1]*(main_list.count(x)-1)/main_list.count(x)

print(len(duplicate))

def remove_duplicate(list):
     u_list = []
     for x in list:
          if u_list.count(x) == 0:
               u_list.append(x)
          else:
               pass
     return u_list

u_duplicate = remove_duplicate(duplicate)

dict_duplicate = {}

for x,y in u_duplicate:
    dict_duplicate[y] = x

sorted_dict = dict(sorted(dict_duplicate.items()))
