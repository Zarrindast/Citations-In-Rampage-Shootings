import os
import pandas as pd
import numpy as np
import urllib
import urllib2
from urllib2 import Request
import requests
from requests import get
import datetime
import re
from bs4 import BeautifulSoup

import copy

import shutil
import subprocess

os.getcwd()
try:
    os.mkdir('/shooterdatalists/shooterdocs')
except OSError:
    print("This directory already exists.")
os.chdir('/shooterdatalists/shooterdocs')

def prettyopen(url_in_quotes):
    page = urllib2.urlopen(url_in_quotes)
    soup = BeautifulSoup(page)
    soup.prettify
    return soup

soup = prettyopen("https://schoolshooters.info/original-documents")

# will be discarded in favor of names_Docs_Ungrouped
templist = list()
# will be a list of all of the links we need to open and scrape
linkslist = list()
# will be a list of all the shooters from this site
fileslist = list()
# list of all files
nameslist = list()
# will be list of indices at which to divide a later list
split_Here = list()
# list of all shooters and all links
names_Docs_Ungrouped = list()
# list of shooter+links groups
names_Docs_Grouped = list()

# find links within the object "site" (the orig docs page from online)
all_links = soup.find_all("a")
for a in all_links:
    templist.append(a.get("href"))

#remove unwanted artifact values
names_Docs_Ungrouped = templist[templist.index(u'/pekka-eric-auvinen'):]
names_Docs_Ungrouped.pop()

linktag = "http"

# write URLs and shooter names to backup lists in case I somehow go nuclear; makes 1 file + one env obj for each list
f = open('linkslist.txt','w+')
g = open('nameslist.txt', 'w+')
f,g
# write to file; append links to empty list
for item in names_Docs_Ungrouped:
    if linktag in item:
        f.write(item + "\n"); linkslist.append(item)
    else:
        g.write(item[1:] + "\n"); nameslist.append(item[1:])
        # indices in names_Docs_Ungrouped of all elements appearing in nameslist
        # we will split up names_Docs_Ungrouped at these indices
        # in order to segregate the documents by association with a shooter
        split_Here.append(names_Docs_Ungrouped.index(item))
        names_Docs_Ungrouped[names_Docs_Ungrouped.index(item)] = names_Docs_Ungrouped[names_Docs_Ungrouped.index(item)][1:]

# close 'em
f.close(), g.close()

# we're gonna be mutilating the ungrouped list; let's mutilate a mere copy
names_Docs_Ungrouped_Copy = copy.deepcopy(names_Docs_Ungrouped)
# we are going to create a list whose entries are
# [shooter1, shooter1doc1, shooter1doc2, ...],[shooter 2, shooter2doc1, ...], ...
names_Docs_Grouped = [None] * len(split_Here)
# we will segment the original list at the "shooter's name" entries
# going backwards, for ease of coding
N = len(split_Here)-1
while N >= 0:
    names_Docs_Grouped[N] = names_Docs_Ungrouped_Copy[split_Here[N]:]
    # get rid of the elements put into names_Docs_Grouped[N]
    names_Docs_Ungrouped_Copy = names_Docs_Ungrouped_Copy[:split_Here[N]]
    # move back an entry in names_Docs_Grouped
    N = N-1

# use quotes around the desired filename
def writelist(somelist, target_in_quotes):
    f = open(target_in_quotes, 'w+')
    x = 0
    while x < len(somelist):
        f.write(somelist[x] + "\n")
        x = x + 1
    f.close()

def writelistoflists(somelist, target_in_quotes):
    f = open(target_in_quotes, 'w+')
    x = 0
    while x < len(somelist):
        y = 0
        while y < len(somelist[x]):
            f.write(somelist[x][y]+"\n")
            y = y + 1
        f.write("\n")
        x = x + 1
    f.close

def download(url, file_name):
    with open(file_name, "w+") as file:
        # get request
        response = get(url)
        #write to file
        file.write(response.content)

# download the pdfs into an organized file set; remove the links that are not pdfs 
# HERE WE GO

all_shooters = '/shooterdatalists/origdocs'
os.chdir(all_shooters)
cutoff = len("https://schoolshooters.info/sites/default/files/")
fileslist = list()
fileslist = [None] * len(names_Docs_Grouped)

x = 0
while x < len(names_Docs_Grouped):
    fileslist[x] = list()
    fileslist[x].append(names_Docs_Grouped[x][0])
    y = 1
    while y < len(names_Docs_Grouped[x]):
        # is this even a document to process? if not, get rid of it and tell me.
        if "pdf" not in names_Docs_Grouped[x][y].lower():
            print "names_Docs_Grouped[{},{}] is not a pdf, see url below:".format(x,y); print(names_Docs_Grouped[x][y])
            del names_Docs_Grouped[x][y]
        else:
            # do we need a folder for this shooter?
            if not os.path.exists(names_Docs_Grouped[x][0]):
                # then make one
                os.mkdir(names_Docs_Grouped[x][0])
            fileslist[x].append(str(names_Docs_Grouped[x][y][cutoff:]))
            # make sure we're not downloading a document twice
            if not os.path.exists("{}/{}".format(names_Docs_Grouped[x][0],str(names_Docs_Grouped[x][y][cutoff:]))):
                # then download it
                download(names_Docs_Grouped[x][y], "{}/{}".format(names_Docs_Grouped[x][0],str(names_Docs_Grouped[x][y][cutoff:])))
        y = y + 1
    x = x + 1
