
#Goal: Create a script that automatically downloads the most recent Our Super Adventure comic from a static html page and save it to a local directory with the incremented number and name of the comic.

#Comic is deployed on Monday so the bot should run on that day.

#Created by Jon Thornton on 10/6/2019

from bs4 import BeautifulSoup
import shutil
import requests
import datetime

#Calls the website to pulldown HTML content
# page = requests.get('https://www.oursuperadventure.com/')
# content = page.text
# soup = BeautifulSoup(content, 'html.parser')

# print()

# raw_tag = soup.find("div", { "id" : "comic" }).find("img", recursive=False)
# title = raw_tag.get('title')
# img_src = raw_tag.get('src')

title = 'Sleepyhead (30th September, 2019)'
img_src = 'https://www.oursuperadventure.com/wp-content/uploads/2019/09/OSA3-036-Sleepyhead.jpg'

# print (raw_tag)
print(title)
print(img_src)

#Need to pull date out of the 'title' of the comic
#Use string manupulation to find the values between the parenthesesis
foo = title.split('(')[1]
foo = foo.split(')')[0]
print(foo)



#Use date library to convert string date to MM-dd-yyyy format


# #Throws a request to pull down the image
# print('Requesting image')
# response = requests.get(img_src, stream=True)

# #Saves the file to a local directory with the name of the file.
# print('Downloading Image')
# filename = '{0} - {1}'.format(date, img_name)
# with open(filename, 'wb') as out_file:
#     shutil.copyfileobj(response.raw, out_file)

# #Deletes the active response and closes the connection.
# print('Completed Download')
# del response