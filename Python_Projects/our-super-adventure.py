
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

print()

raw_tag = soup.find("div", { "id" : "comic" }).find("img", recursive=False)
title_tag = raw_tag.get('title')
img_src = raw_tag.get('src')

#Test Case to pull down text for string manipulation
# title_tag = 'Sleepyhead (30th September, 2019)'
# img_src = 'https://www.oursuperadventure.com/wp-content/uploads/2019/09/OSA3-036-Sleepyhead.jpg'

#Test Case from October 7th, 2019 with different formatting
title_tag = 'Compliments (October 7th, 2019)'
img_src = 'https://www.oursuperadventure.com/wp-content/uploads/2019/10/OSA3-037-Compliments.jpg'

# print (raw_tag)
print(title_tag)
print(img_src)

#Need to pull date out of the 'title' of the comic
#Use string manipulation to find the values between the parenthesesis
comic_name = title_tag.split('(')[0][:-1]
date = title_tag.split('(')[1][:-1]
date = date.split(' ')
day = date[1][:-3]
month = date[0]
year = date[2]
#Use datetime library to convert string date to YYYY-MM-dd format
date = '{0}-{1}-{2}'.format(date[0],date[1][:-3],date[2])

d = datetime.strptime(date, '%B-%d-%Y')
date = d.strftime('%Y-%m-%d')


#Throws a request to pull down the image
print('Requesting image')
response = requests.get(img_src, stream=True)

#Saves the file to a local directory with the name of the file.
print('Downloading Image')
filename = '{0} - {1}.png'.format(date, comic_name)
with open(filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

#Deletes the active response and closes the connection.
print('Completed Download')
del response