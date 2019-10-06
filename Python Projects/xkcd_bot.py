
#Goal: Create a script that automatically downloads the most recent XKCD comic from a static html page and save it to a local directory with the incremented number and name of the comic.

#Created by Jon Thornton on 10/6/2019

import shutil
import requests
import re

#Calls the website to pulldown HTML content
page = requests.get('https://xkcd.com/')
content = page.text

# Test Case from the attributes in the meta tags. All the content is at the top of the html doc. 
# content = '<meta property="og:title" content="College Athletes"> <meta property="og:url" content="https://xkcd.com/2210/"> <meta property="og:image" content="https://imgs.xkcd.com/comics/college_athletes_2x.png"> <meta name="twitter:card" content="summary_large_image">'

#Using Regex, parse out the high res Image.
try:
    #Alt Attribute contains the formal comic name.
    img_name = re.search('<meta property="og:title" content="(.+?)">', content).group(1) + '_2x.png'
    comic_num = re.search('<meta property="og:url" content="https://xkcd.com/(.+?)/">', content).group(1)

    #Finds high res link off HTML call
    img_link = 'https://imgs.xkcd.com/comics/' + re.search('<meta property="og:image" content="https://imgs.xkcd.com/comics/(.+?)_2x.png">', content).group(1) + '_2x.png'
except AttributeError:
    print('Failed to load in the data')

#Throws a request to pull down the image
print('Requesting image')
response = requests.get(img_link, stream=True)

#Saves the file to a local directory with the name of the file.
print('Downloading Img')
filename = '{0} - {1}'.format(comic_num, img_name)
with open(filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

#Deletes the active response and closes the connection.
print('Completed Download')
del response
