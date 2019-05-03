# Don't be me and get yourself in this situation! I had to use some ungodly code to reconstruct an organized table from
# an ill-concieved set of notes.

# Having forgotten to evaluate the quality of the pdfs in the first place...

# I went through and marked with an asterisk all of the documents that were sufficiently legible under the conversion.
# I used PYTESSERACT to OCR the remainder of the files, visually inspected those, and marked them the same way.
# Finally, files that were not handled by those two methods, I used voice-to-text technology to recreate rather than attempt to teach
# the computer to process everyone's handwriting individually.

import shutil
import os
import os.path
import subprocess

os.chdir("/shooterdatalists/")
# pull two-column table out of the saved-asfiles.txt. col "do" is OCR and/or H and/or * ; col "name" is the corr. file
processing_table = pd.read_table('saved-asfiles.txt', delim_whitespace=True, names=('do','name'), dtype={'do': 'str','name': 'str'})
processing_table = pd.read_table('file_processing_table.csv', delim_whitespace=False, names=('name','P2Tfile','stat_after_P2T','tessfile','stat_after_tess','handwritten','notes'), dtype={'name': 'str','P2Tfile': 'str','stat_after_P2T': 'str','tessfile': 'str','stat_after_tess': 'str','handwritten': 'str','notes': 'str'})
# restrict to rows (it's going to be unique though) w/ appropriate file under "name"
# set up for the handwriting/hand-check list and the general "check into this / error thrown" list

x = 0
while x < len(fileslist):
    # handwriting list will be broken into sublists by shooter, as we have been doing
    handwrittenfiles_list[x] = list(); handwrittenfiles_list[x].append(fileslist[x][0])
    # general check this list will be broken into sublists by shooter as well
    process_error_files_list[x] = list(); process_error_files_list[x].append(fileslist[x][0])
    # just to make the output sectioned and easier to read
    print "----------------------{}----------------------".format(fileslist[x][0])
    # start in shooterdatalists/origdocs/shooter-name as folder
    folder = "/shooterdatalists/origdocs"
    # need to have this script accessible-- need to figure out where to keep it so it's globally accessible
    shutil.copy2('/shooterdatalists/multipage-ocr.py' , folder)
    os.chdir(folder)
    y = 1
    while y < len(fileslist[x]):
        try:
            # more output readability sectioning-- subsections by file now
            print "-----{}".format(fileslist[x][y])
            # iterating through all shooters and their associated files,
            # temporarily consider the row containing a given file (row currently = filename and status)
            ## code cleanup note: replace x[x[""]] == ] with more concise expression
            filexy_row_temp = processing_table[processing_table["name"] == fileslist[x][y]]
            # now let's examine the status we indicated for that particular file
            filexy_dostring_temp = (filexy_row_temp["do"].tolist())[0]
            # test status for the presence of various instructions
            # where * indicates done
            # OCR indicates need for tesseracting (already tried PDF2TXT at this point)
            if 'OCR' in filexy_dostring_temp:
                if not os.path.isfile("txt/{}/checkme_{}".format(fileslisttxt[x][0], fileslisttxt[x][y], fileslisttxt[x][0], fileslisttxt[x][y])):
                    ## code cleanup note: prompt user to authorize the tesseract OCR processing in below commented-out line
                    # subprocess.call("python /Users/programming/Python/multipage-ocr.py -i {}/{} stdout -o txt/{}/checkme_{}".format(fileslist[x][0], fileslist[x][y], fileslist[x][0], fileslisttxt[x][y]), shell=True)
                    print "OCR processing attempted."
                else:
                    print "OCR'ing was already done, cool."
            # handwriting list recieves appropriate files and it is noted in output
            if 'H' in filexy_dostring_temp:
                handwrittenfiles_list[x].append(fileslist[x][y])
                print "Added to Handwritten list."
            # already-processed files and partially-processed files are noted in output
            if '*' in filexy_dostring_temp:
                print "At least some of this document was already done."
                if filexy_dostring_temp == "*":
                    print "In fact, all of it was!"
            # files we threw away are noted in output (they're still in the lists right now)
            if 'X' in filexy_dostring_temp:
                print "This file deemed irrelevant."
            # all files should have had one of those markings. if not...
            if not (('OCR' in filexy_dostring_temp) or ('H' in filexy_dostring_temp) or ('*' in filexy_dostring_temp) or ('X' in filexy_dostring_temp)):
                print "{} has not been marked for processing; go fix it in the list.".format(fileslist[x][y])
        # only error I've gotten so far, but
        ## code cleanup note: handle all possible errors (is there a "general error" term to except?)
        except IndexError:
            # just gonna have to look into this manually if it happens.
            process_error_files_list.append("{}".format(fileslist[x][y]))
            print "Check whether {} is really in the saved-asfile.txt list.".format(fileslist[x][y])
        y = y + 1
    x = x + 1


