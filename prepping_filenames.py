import os

os.chdir("shooterdatalists")
processing_table = pd.read_csv('file_processing_table.csv')
os.chdir("origdocs/txt")

# go through all directories. for all files named checkme_, change to tess_.
# TWO EQUALLY GOOD WAYS-- DEPENDING ON HOW DEEP THE DIRECTORIES GO

# if only a couple deep:

x = 0
while x < len(fileslist):
    os.chdir("/shooterdatalists/origdocs/txt/{}".format(fileslist[x][0]))
    for file in os.listdir("."):
        if file.startswith("checkme_"):
            os.rename(file, "tess_{}".format(file[8:]))
    x = x + 1

# if supa deep:

for dir in os.listdir("/shooterdatalists/origdocs/txt")[1:]:
    for file in os.listdir("/shooterdatalists/origdocs/txt/{}".format(dir)):
        if file.startswith("checkme_"):
           os.rename("/shooterdatalists/origdocs/txt/{}/{}".format(dir, file), "/shooterdatalists/origdocs/txt/{}/tess_{}".format(dir,file[8:]))


# Now make a list of "current" files, to replace fileslisttxt which we have been primarily
# using, where the files are named appropriately such that the correct version is retrieved
# according to the processing table. 

# I am reluctant to simply delete the bad files and reassign those filenames to the corresponding good files, bc 
# 1) bad files generally take up very little space and are mostly blank, so the cost of leaving them is just organizational,
# 2) if rerunning the OCR scripts, they will search for the original names
# 3) if I want to go back and check what was wrong with certain processings, it would be more convenient to have them onhand.


# modify so you can run fowards or backwards: col_number needs to start at len(table.columns)-1 and go to 0 via
# col_number = col_number + 1.
def first_occurance(table, rowlabel, whole_or_part, desired_value, list, dictionary):
    whole = lambda a, b: a is b
    part = lambda a, b: a in b
    # Hey, please don't lift this code as an outline for anything with user input!
    # I'm only using eval because I am the only person invoking it, inside this script!
    # https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
    testfor = lambda a, b, c: eval("c(a,b)")
    col_number = 0
    while col_number < len(table.columns):
        entry = table.loc[rowlabel, table.columns[col_number]]
        # if the desired value IS or IS IN (depending on which you picked) entry row = rowindex, col = col_number
        if testfor(desired_value, entry, whole_or_part):
            # put whatever indicator of this we want, into our list
            list.append(dictionary[table.columns[col_number]])
            # and once we find the occurance, we can stop for that row.
            break
        # keep going through the columns until we find it.
        col_number = col_number + 1

# convenience
pc = processing_table
# beware, because you can no longer treat "name" like a normal column after this:
pc.set_index("name", inplace = True)
# fill null values because it was messing up first_occurance iterating over the entries.
pc = pc.fillna('pending')
fileslist_ready = list()
# prepare list fileslist_ready to hold files to search for citations
fileslist_ready = [None] * len(fileslistpdf)
x = 0
while x < len(fileslistpdf):
    # segment up fileslist_ready by shooter, starting each sublist with the shooter's name
    fileslist_ready[x] = []
    fileslist_ready[x].append(fileslistpdf[x][0])
    # we already dealt with the y = 0 case
    y = 1
    while y < len(fileslistpdf[x]):
        # designate the txt version of the file in question (same name as the P2T proc'd version)
        file = fileslistpdf[x][y][:len(fileslistpdf[x][y])-3]+"txt"
        # dict gives the various processed versions of the file
        # the places where a finished file could be first indicated, based on the way I made the table
        # P2T only says bad/usable/DNE
        dict = {"stat_after_P2T": file, "tessfile": "tess_{}".format(file), "handwritten": "hand_{}".format(file)}
        # "assuming the file's versions are charted at all,"
        if fileslistpdf[x][y] in pc.index:
            # find the first instance of a "*" marking to indicate the correct file processing to append
            # to the list of files to search for citations
            first_occurance(pc, fileslistpdf[x][y], part, "*", fileslist_ready[x], dict)
            # if the table indicates there is a transcribed handwriting sample (possibly "as well"),
            if pc.loc[fileslistpdf[x][y], "handwritten"] == "*":
                # include it in the list of files to search for citations
                fileslist_ready[x].append(dict["handwritten"])
        # move on to next file for the same shooter/sublist
        y = y + 1
    x = x + 1

# At this point, I was getting a typeerror saying float not iterable. After some StackOverflowing I figured out
# that it was my null entries in pc (processing_table) causing the error. Thus I went back and did the pc.fillna('pending') above.
