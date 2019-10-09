
#Goal: Create a script that automatically downloads the most recent Poorly Drawn Lines comic from a static html page and save it to a local directory with the incremented number and name of the comic.

#Comic is released on Monday/Wednesday/Fridays

#Created by Jon Thornton on 10/8/2019

from datetime import datetime
from bs4 import BeautifulSoup
import shutil
import requests

#Calls the website to pulldown HTML content
page = requests.get('http://www.poorlydrawnlines.com/comic/pond/')
content = page.text
soup = BeautifulSoup(content, 'html.parser')

#Pull out comic information from div with Id="comic"
comic_tag = soup.find('figure', { 'class' : 'wp-block-image' })
comic_name = soup.title.string[21:]

# print(comic_name)
comic_name = ''.join(e for e in comic_name if e.isalnum())
img_src = comic_tag.find('img').get('src')

#Throws a request to pull down the image
print('Requesting Image')
response = requests.get(img_src, stream=True)

#Saves the file to a local directory with the name of the file.
print('Downloading Image')
filename = '{0}.png'.format(comic_name)
with open(filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

#Deletes the active response and closes the connection.
print('Completed Download')
del response