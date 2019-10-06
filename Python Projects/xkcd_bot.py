
#Goal: Create a script that automatically downloads the most recent XKCD comic from a static html page and save it to a local directory with the incremented number and name of the comic.

#Created by Jon Thornton on 10/5/2019

import shutil
import requests
import re

text = '<img src="//imgs.xkcd.com/comics/hours_before_departure.png" title="They could afford to cut it close because they all had Global Entry." alt="Hours Before Departure" srcset="//imgs.xkcd.com/comics/hours_before_departure_2x.png 2x">'


try:
    img_name = re.search('srcset="//imgs.xkcd.com/comics/(.+?)_2x.png', text).group(1) + '_2x.png'
    img_link = 'https://imgs.xkcd.com/comics/' + re.search('srcset="//imgs.xkcd.com/comics/(.+?)_2x.png', text).group(1) + '_2x.png'
except AttributeError:
    print('Failed to load in the data')
print('foo')
print('Requesting image')
response = requests.get(img_link, stream=True)

print('Downloading Img')
with open(img_name, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

print('Completed Download')
del response
