""" Problem:
    Download and change desktop wallpapers automatically 
"""
import requests as rq
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = rq.get(api_url)

content = response.content.decode('UTF-8')

#convert string to json

dict_content = json.loads(content)

#get image URL

#print(dict_content.keys())
image_url = dict_content['hdurl']

#download image
res = rq.get(image_url)

#save the image

with open('./apod.png','wb') as image:
    image.write(res.content)

# set as wallpaper
PyWallpaper.change_wallpaper('/Users/rahimhossain/Documents/codes/OOP/apod.png')
