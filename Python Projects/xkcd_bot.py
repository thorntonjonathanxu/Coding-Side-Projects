
#Goal: Create a script that automatically downloads the most recent XKCD comic from a static html page and save it to a local directory with the incremented number and name of the comic.

#Comic is deployed on Monday/Wednesday/Fridays so the bot should run on those days.

#Created by Jon Thornton on 10/6/2019
from bs4 import BeautifulSoup
import shutil
import requests

# Calls the website to pulldown HTML content
page = requests.get('https://xkcd.com/')
content = page.text
soup = BeautifulSoup(content, 'html.parser')

#Test Cases for link specific information
# soup = BeautifulSoup('<meta content="Hours Before Departure" property="og:title"/>')
# soup = BeautifulSoup('<meta content="https://xkcd.com/2211/" property="og:url"/>')
# soup = BeautifulSoup('<meta content="https://imgs.xkcd.com/comics/hours_before_departure_2x.png" property="og:image"/>')

#Generates the content from ba
img_name = soup.find(property="og:title").get('content')
comic_num = soup.find(property="og:url").get('content')[-5:-1] #Must pull in a 4 digit number or will break
img_link = soup.find(property="og:image").get('content')

print(img_name)
print(comic_num)
print(img_link)

print('Requesting image')
response = requests.get(img_link, stream=True)

#Saves the file to a local directory with the name of the file.
print('Downloading Image')
filename = '{0} - {1}.png'.format(comic_num, img_name) #File needs to be a PNG format
with open(filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

#Deletes the active response and closes the connection.
print('Completed Download')
del response
