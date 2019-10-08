
#Goal: Create a script that automatically downloads the most recent Our Super Adventure comic from a static html page and save it to a local directory with the incremented number and name of the comic.

#Comic is deployed on Monday so the bot should run on that day.

#Created by Jon Thornton on 10/6/2019

from datetime import datetime
from bs4 import BeautifulSoup
import shutil
import requests

#Calls the website to pulldown HTML content
page = requests.get('https://www.oursuperadventure.com/')
content = page.text
soup = BeautifulSoup(content, 'html.parser')

#Pull out comic information from div with Id="comic"
comic_tag = soup.find('div', { 'id' : 'comic' }).find('img', recursive=False)
comic_name = comic_tag.get('title').split(' ')[0]
img_src = comic_tag.get('src')
date = soup.find('span',{'class' : 'post-date'}).string #Date is in a span class

#Use datetime library to convert string date to YYYY-MM-dd format
d = datetime.strptime(date, '%B %d, %Y')
date = d.strftime('%Y-%m-%d')

#Throws a request to pull down the image
print('Requesting Image')
response = requests.get(img_src, stream=True)

#Saves the file to a local directory with the name of the file.
print('Downloading Image')
filename = '{0} - {1}.png'.format(date, comic_name)
with open(filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

#Deletes the active response and closes the connection.
print('Completed Download')
del response