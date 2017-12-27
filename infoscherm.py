#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os
# The path of the images are speficed and using listdir function os we get the list of images. Inorder to filter other file have used 'endswith' in this case i have used only *.jpg files. Then append them to list and pass them to
# update screen functionality.
def get_images():
    data_list=[]
    path='/home/pi/rpi-infoscherm/img/' # specifiy path to directory that hosts images
    dirs = os.listdir(path)
    #append list with files ending with .jpg format
    for name in dirs:
        if name.endswith(".jpg"):
            data_list.append(path+name)
            for content in data_list:
                print content
    print 'lijst: ' + str(data_list)
    data = ' '.join(data_list)
    #data_list = str(data_list.strip(',[]'))
    command = "sudo fbi -a --noverbose -T 1 -u -t 30 --blend 1000 "+ str(data)
    print command
    return command

def commands():
    os.system("sudo killall fbi")
    command = get_images()
    os.system(command)


if __name__=='__main__':
    commands()

