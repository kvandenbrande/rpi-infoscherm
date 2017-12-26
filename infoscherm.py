#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys,os
Color=(120, 40, 130)

class change_image():
# Pygame initialization of pygma and setting up of the screen size and color
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Image Viewer")

		self.size=self.width,self.height=700,500
		self.screen=pygame.display.set_mode(self.size)
		self.screen.fill((Color))
		self.load_image()

#The actual funtion to load an image and blit on screen and the screen is frozen for 2 seconds, this gives the effect of slideshow. The time can be varied cby changing the wait time

	def update_image(self,name):
		 self.name=name
		 self.image=pygame.image.load(self.name)

		 self.screen.fill(Color)
		 pygame.display.update()
		 self.screen.blit(self.image,(0,0))
		 #pygame.display.flip()

		 pygame.display.update()
                 pygame.time.wait(30000) # Use your custom time defaulted to 2 sec
		 return True


# The path of the images are speficed and using listdir function os we get the list of images. Inorder to filter other file have used 'endswith' in this case i have used only *.jpg files. Then append them to list and pass them to update screen functionality.	
 
	def load_image(self):
		data_list=[]
		path='/home/pi/rpi-infoscherm/img/' # specifiy path to directory that hosts images
		dirs = os.listdir(path)
	#append list with files ending with .jpg format
		for name in dirs:
			if name.endswith(".jpg"):
				data_list.append(name)

		for content in data_list:
			#print content
			self.update_image(content)
				
	
# the main function 
	def main(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

if __name__=='__main__':
	obj=change_image()
	obj.main()

