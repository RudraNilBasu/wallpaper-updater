import os
import time

from os import listdir
from os.path import isfile, join

path = "/home/administrator/Downloads/wallpaper"

pictures = os.listdir(path)

current_index = -1
wait_time = 20 # seconds

def apply_wallpaper(name):
	os.system("gsettings set org.gnome.desktop.background picture-uri file://" + path + "/" + name)

def get_random_picture():
	global current_index
	current_index = current_index + 1
	return pictures[(current_index) % len(pictures)]

while True:
	picture = get_random_picture()
	print picture
	apply_wallpaper(picture)
	time.sleep(wait_time)
