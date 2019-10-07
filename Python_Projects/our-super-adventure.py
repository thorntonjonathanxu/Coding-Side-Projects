
#Goal: Create a script that automatically downloads the most recent Our Super Adventure comic from a static html page and save it to a local directory with the incremented number and name of the comic.

#Comic is deployed on Monday so the bot should run on that day.

#Created by Jon Thornton on 10/6/2019

from bs4 import BeautifulSoup
import shutil
import requests
import re

#Calls the website to pulldown HTML content
# page = requests.get('https://www.oursuperadventure.com/')
# content = page.text
# soup = BeautifulSoup(content, 'html.parser')

# print(content)
# soup = BeautifulSoup('[<div id="comic"> <img src="https://www.oursuperadventure.com/wp-content/uploads/2019/09/OSA3-036-Sleepyhead.jpg" alt="Sleepyhead (30th September, 2019)" title="Sleepyhead (30th September, 2019)">	</div>]')

foo = soup.find_all(id="comic")
tag = soup.img
print(tag)
# for line in foo:
    # print(line)

# print(soup)
#     #Meta tags contains the formal comic name and innumerated comic number.
#     div_block = re.search('<div id="comic">\n(.*)\n</div>', content).group(1)

#     # img_name = re.search('<meta property="og:title" content="(.+?)">', content).group(1) + '_2x.png'
#     # comic_num = re.search('<meta property="og:url" content="https://xkcd.com/(.+?)/">', content).group(1)

#     # #Finds high res link off HTML call
#     # img_link = 'https://imgs.xkcd.com/comics/' + re.search('<meta property="og:image" content="https://imgs.xkcd.com/comics/(.+?)_2x.png">', content).group(1) + '_2x.png'

# except AttributeError:
#     print('Failed to load in the data')


# print(div_block)

#Copied code from xkcd_bot.py

# #Throws a request to pull down the image
# print('Requesting image')
# response = requests.get(img_link, stream=True)

# #Saves the file to a local directory with the name of the file.
# print('Downloading Img')
# filename = '{0} - {1}'.format(comic_num, img_name)
# with open(filename, 'wb') as out_file:
#     shutil.copyfileobj(response.raw, out_file)

# #Deletes the active response and closes the connection.
# print('Completed Download')
# del response
