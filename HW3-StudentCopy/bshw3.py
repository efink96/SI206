# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import re

fout = open('webpage.html', 'w')
fileinfo = urllib.request.urlopen('http://www.collemc.people.si.umich.edu/data/bshw3StarterFile.html').read()
soup = BeautifulSoup(fileinfo, 'html.parser')
data = soup.prettify()
data = data.replace('student', 'AMAZING student')
data = data.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', 'bshw3picture.jpg')
data = data.replace('logo2.png', 'media/logo.png')
fout.write(data)