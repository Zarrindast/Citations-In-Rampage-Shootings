# OCR code

# install tesseract-ocr for python here: https://github.com/tesseract-ocr/tesseract/wiki
# download multipage pdf to txt OCR (tesseract-based) here: https://github.com/qedsoftware/multipage-ocr
# example
# python /Users/programming/Python/multipage-ocr.py -i shooterdatalists/origdocs/charles-whitman/Whitman_autopsy.pdf stdout

import os
x = 0
while x < len(fileslist):
  # start in shooterdatalists/origdocs/shooter-name as folder
  folder = "/shooterdatalists/origdocs/{}".format(fileslist[x][0])
  # e.g. folder = "/shooterdatalists/origdocs/charles-whitman"
  os.chdir(folder)
  y = 0
  while y < len(fileslist[x]):
    python /Users/programming/Python/multipage-ocr.py -i fileslist[x][y] stdout
    y = y + 1
  x = x + 1

/Users/programming/Python/multipage-ocr.py file stdout
# after all files done, delete multipage-ocr.py from folder
# return to shooterdocs/origdocs
