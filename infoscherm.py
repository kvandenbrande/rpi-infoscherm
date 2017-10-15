#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import time
import sys
import os
import subprocess
import json
from subprocess import Popen
from pygame.locals import *

pygame.init()

# configfile
##try:
##    with open('/home/pi/Desktop/infoscherm_conf.json', 'r') as f:
##        config = json.load(f)
##except ValueError:
##     print 'Error: Decoding config has failed'
##
##LOCATION = config['LOCATION']['vestiging']
##LOCATION_DETAIL = config['LOCATION']['locatie']

# run check
try:
    with open("./online.tmp", "w") as processid:
        processid.write(str(os.getpid()))
except IOError:
    print "Error: online.tmp cannot be made."

STARTUP = pygame.font.SysFont('monospace', 25)
TEXT = pygame.font.SysFont('roboto', 35, bold=True)
TITLE = pygame.font.SysFont('roboto', 50, bold=True)
TITLE1 = pygame.font.SysFont('roboto', 75, bold=True)
WHITE = (255, 255, 255)
WAITTIME = 30  # default time to wait between images (in seconds)
THICKNESS = 10

# media files
LOCALEPATH = '/home/pi/infoscherm/img/'

# set up the window, max screensize, fullscreen no frames

modes = pygame.display.list_modes()
screen = pygame.display.set_mode(max(modes), pygame.NOFRAME)
pygame.mouse.set_visible(False)
(x, y) = screen.get_size()

# locations
# TV Waasland resolutie 1920x1080 as refence to other resolutions

L_STARTUP_X = 700 * x / 1920
L_STARTUP_Y = 540 * y / 1080
L_WELCOME_X = 150 * x / 1920
L_WELCOME_Y = 800 * y / 1080
L_LOGO_X = 1350 * x / 1920
L_LOGO_Y = 800 * y / 1080
L_BORDER_AX = 100 * x / 1920
L_BORDER_AY = 100 * y / 1080
L_BORDER_BX = 1600 * x / 1920
L_BORDER_CY = 900 * y / 1080
L_EVENT_X = 150 * x / 1920
L_EVENTN_Y = 300 * y / 1080
L_EVENTT_Y = 500 * y / 1080
L_EVENTL_Y = 700 * y / 1080
L_KA_TITEL_X = 150 * x / 1920
L_KA_TITEL_Y = 150 * y / 1080


# startup screen

label = STARTUP.render('... warming up, please wait ...', 5, WHITE)
screen.blit(label, (L_STARTUP_X, L_STARTUP_Y))
pygame.display.flip()

# image config

#transparant = pygame.image.load(LOCALEPATH + 'logo.png').convert_alpha()
img1 = pygame.image.load(LOCALEPATH + '1.jpg')
img1 = img1.convert()
img1 = pygame.transform.scale(img1, max(modes))
img2 = pygame.image.load(LOCALEPATH + '5.jpg')
img2 = img2.convert()
img2 = pygame.transform.scale(img2, max(modes))
img3 = pygame.image.load(LOCALEPATH + '6.jpg')
img3 = img3.convert()
img3 = pygame.transform.scale(img3, max(modes))
img4 = pygame.image.load(LOCALEPATH + '9.jpg')
img4 = img4.convert()
img4 = pygame.transform.scale(img4, max(modes))



# run the loop

while True:
    # startscherm
    
    # tekenen van welkom scherm ipv afbeelding
    
    screen.fill(0, 0, 0)

##    pygame.draw.line(screen, WHITE, (L_BORDER_AX - THICKNESS / 2 + 1,
##                     L_BORDER_AY), (L_BORDER_BX, L_BORDER_AY),
##                     THICKNESS)
##    pygame.draw.line(screen, WHITE, (L_BORDER_AX, L_BORDER_AY),
##                     (L_BORDER_AX, L_BORDER_CY), THICKNESS)
##    pygame.draw.line(screen, WHITE, (L_BORDER_AX - THICKNESS / 2 + 1,
##                     L_BORDER_CY), (L_BORDER_BX, L_BORDER_CY),
##                     THICKNESS)
##    pygame.draw.line(screen, WHITE, (L_BORDER_BX - THICKNESS / 2,
##                     L_BORDER_AY), (L_BORDER_BX - THICKNESS / 2,
##                     L_BORDER_CY), THICKNESS)



    # events
    # if check connection to mysql else goto reclame
    # if check event available in mysql else goto reclame
    # for each event teken event scherm
    
##    teller = 0
##    count = 0
##    try:
##        (events, count) = get_events(LOCATION,LOCATION_DETAIL)
##    except:
##        pass
##     
##    while count > 0:
##        screen.fill(load_background())
##        pygame.draw.line(screen, WHITE, (L_BORDER_AX - THICKNESS / 2 + 1, L_BORDER_AY),(L_BORDER_BX, L_BORDER_AY), THICKNESS)
##        pygame.draw.line(screen, WHITE, (L_BORDER_AX,L_BORDER_AY), (L_BORDER_AX,L_BORDER_CY), THICKNESS)
##        pygame.draw.line(screen, WHITE, (L_BORDER_AX - THICKNESS / 2 + 1, L_BORDER_CY),(L_BORDER_BX, L_BORDER_CY), THICKNESS)
##        pygame.draw.line(screen, WHITE, (L_BORDER_BX - THICKNESS / 2, L_BORDER_AY),(L_BORDER_BX - THICKNESS / 2,L_BORDER_CY), THICKNESS)
##
##        # render text
##        titelevent = TITLE.render(events[teller][0], 5, WHITE)
##        screen.blit(titelevent, (L_EVENT_X, L_EVENTN_Y))
##        starttime = TITLE.render(events[teller][1], 5, WHITE)
##        screen.blit(starttime, (L_EVENT_X, L_EVENTT_Y))
##        location = TITLE.render(events[teller][2], 5, WHITE)
##        screen.blit(location, (L_EVENT_X, L_EVENTL_Y))
##
##        # add logo
##        screen.blit(logo, pygame.rect.Rect(L_LOGO_X, L_LOGO_Y,128, 128))
##        pygame.display.flip()
##        time.sleep(WAITTIME)
##        count = count - 1
##        teller = teller + 1

    # images
    screen.blit(img1, (0, 0))
    pygame.display.flip()
    time.sleep(WAITTIME)
    screen.blit(img2, (0, 0))
    pygame.display.flip()
    time.sleep(WAITTIME)
    screen.blit(img3, (0, 0))
    pygame.display.flip()
    time.sleep(WAITTIME)
    screen.blit(img4, (0, 0))
    pygame.display.flip()
    time.sleep(WAITTIME)

