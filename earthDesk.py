#Name: earthDesk.py
#Author: Anthony Critelli, www.acritelli.com
#A script to download images from reddit.com/r/earthporn and save them to a folder.
#The folder can then be used for your desktops

from __future__ import print_function
import urllib2
import sys
import re
import time

#Functions
def downloadImage(link, savePath):
	try:
		response = urllib2.urlopen(link)
	except urllib2.URLError, e:
		print("Problem downloading " + link + " urllib2.URLError: " + str(e), file=sys.stderr)
		return

	if response.getcode() != 200:
		print("Problem downloading " + link + " Response code: " + response.getcode(), file=sys.stderr)
		return
	else:
		ofile = open(savePath, 'wb')
		ofile.write(response.read())
		ofile.close
		return

##Variables
downloadPage = "http://www.reddit.com/r/earthporn/" #Page to be downloaded from reddit
imageFName = time.strftime("%m%d%Y_") #Filename format. Current it's MonthDayYear_XX
savePath = "\\Users\\JohnDoe\\desktopBackgrounds\\" #Path to save files. Be sure to add the trailing slash. Ex: \\Users\\JohnDoe\\Pictures\\ or /home/jdoe/pictures/

#We try to grab the reddit page a maximum of 20 times.
#This is to compensate for any failures getting the page. urllib2 was throwing unknown errors on my Windows system, and I figured that it wouldn't hurt to just try a few times.
#The loop tries to get the page, and just trys again upon error. If no error, break out of the loop.
#I know, I should probably figure out why urllib2 was failing. I don't care. I'll just keep trying until it works, or it hits a maximum.

success = 0
for x in range (0, 20):
	try:
		response = urllib2.urlopen(downloadPage)
	except urllib2.URLError, e:
		print("Problem downloading " + downloadPage + " urllib2.URLError: " + str(e), file=sys.stderr)
		continue
	if response.getcode() != 200:
		print("Problem downloading " + downloadPage + " Response code: " + response.getcode(), file=sys.stderr)
		continue
	else:
		success = 1
		break

if(not success):
	print("Getting the page failed 10 times. Exiting.", file=sys.stderr)
	sys.exit()

#Find all title links on the page
search = re.findall('<a class=\"title \".*?href=\"(.*?)\".*?>', response.read())

if search == None:
	print("Regex on site empty. Exiting.", file=sys.stderr)
	sys.exit()

lineIterator = 1
for link in search:

	#Basic file name for saving images: $SAVEPATH/date_X.
	baseFName = savePath + imageFName + str(lineIterator) + "."

	#First, download images that already have extensions (these links are already direct downloads)
	linkSearch = re.search('.*\.(jpg|png)$', link)
	if linkSearch != None:
		downloadImage(link, baseFName + linkSearch.group(1))
		lineIterator += 1
		continue

	#Next, we'll try for imgur links that aren't direct to the image. All Imgur links are downloaded as .png
	linkSearch = re.search('imgur.*/(.*)', link)
	if linkSearch != None:
		downloadImage("http://i.imgur.com/" + linkSearch.group(1) + ".png", baseFName + "png")
		lineIterator += 1
		continue

	print("Skipping: " + link)

print("Successfully downloaded " + str(lineIterator) + " images!")