# for use *after* scraping_Langman.py, depends upon variable def therein

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

# closely following 2 functions from: https://github.com/shakkaist/Python/blob/master/Day2Session2/pdfconverter.py

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension.lower() == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf[0:len(pdf)-4] + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file
			#textFile.close

# long run time
# convert everything to txt
# brenda spencer's aren't converting??


os.chdir('/shooterdatalists/origdocs')

try:
    os.mkdir('txt')
except OSError:
    print("This directory already exists.")
# this could use a function. say mkdirornot()

bogus_List = list()

###### CAUTION: THIS IS VERY SLOW, DON'T RUN IT IF YOU DON'T NEED TO
# finish preventions for redundant conversion.
x = 0
while x < len(fileslist):
    print names_Docs_Grouped[x][0]
    try:
        os.mkdir('/shooterdatalists/origdocs/txt/{}/'.format(names_Docs_Grouped[x][0]))
    except OSError:
        print("This directory already exists.")
    pdfDir = '/shooterdatalists/origdocs/{}/'.format(names_Docs_Grouped[x][0])
    txtDir = '/shooterdatalists/origdocs/txt/{}/'.format(str(names_Docs_Grouped[x][0]).lower())
    try:
        # if not os.path.isfile()
        convertMultiple(pdfDir, txtDir)
    except pdfminer.pdfdocument.PDFEncryptionError:
        print("PDFEncryptionError")
        bogus_List.append(names_Docs_Grouped[x][0])
    except pdfminer.pdfparser.PDFSyntaxError:
        print("Bogus PDF alert.")
        bogus_List.append(names_Docs_Grouped[x][0])
    else:
        print("Conversions completed.")
    x = x + 1

bogus_List
# brenda spencer. luckily she is unlikely to be referring to anyone anyway

##############################

import copy

# our list of files should no longer refer to pdfs.

fileslisttxt = copy.deepcopy(fileslist)
x = 0
while x < len(fileslisttxt):
    y = 1
    while y < len(fileslist[x]):
        fileslisttxt[x] = [s.replace("pdf","txt") for s in fileslisttxt[x]]
        fileslisttxt[x] = [s.replace("PDF","txt") for s in fileslisttxt[x]]
        y = y + 1
    x = x + 1
