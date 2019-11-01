# FINALLY we get to the good part, cross-checking for references!

citations = copy.deepcopy(fileslist_ready)
citations_Short = copy.deepcopy(fileslist_ready)
citations_Blurb = [None]*len(fileslist_ready)

import codecs

# search .txts for names of other shooters.

x = 0
while x < len(fileslist):
    this_shooter = "/shooterdatalists/origdocs/txt/{}".format(fileslist_ready[x][0])
    os.chdir(this_shooter)
    citations_Blurb[x] = []
    citations_Blurb[x].append(fileslist_ready[x][0])
    y = 1
    while y < len(fileslist_ready[x]):
        citations[x][y] = []
        citations[x][y].append(fileslist_ready[x][y])
        citations_Short[x][y] = []
        citations_Short[x][y].append(fileslist_ready[x][y])
        myfile = fileslist_ready[x][y]
        try:
            with codecs.open(myfile, encoding='utf-8') as searchfile:
                for i, line in enumerate(searchfile):
                    z = 0
                    while (z < len(namesearch_Long)):
                        if not (citations[x][0] == namesearch_Long[z][0]):
                        # this doesn't seem to be working
                            q = 0
                            while q < len(namesearch_Long[z]):
                                if namesearch_Long[z][q] in line.lower():
                                    citations[x][y].append([namesearch_Long[z][0], namesearch_Long[z][q], "line {}".format(i), line])
                                    citations_Short[x][y].append(namesearch_Long[z][0])
                                    citations_Blurb[x].append(namesearch_Long[z][0])
                                q = q + 1
                        z = z + 1
        except IOError:
            print("Error in {} folder.".format(citations[x][0]))
        y = y + 1
    x = x + 1


# we will create a list of dictionaries that correspond to individual documents.
# keys: citations within those documents
# values: will be whether the citation is legitimate or a false positive.
# we will be prompted to evaluate each citation.
# if we wish to stop the long process in the middle, we may opt out and have our progress saved to a repository.
# so there are 3 objects between which we are transferring information:
# 1) the total list of citations to be evaluated, without said evaluations attached ("citations") -- will not be altered,
# 2) the object with which we are actively evaluating citations ("cite_dict")-- created as blank and will be altered, and
# 3) the storage repository of already evaluated citations ("cite_dict_storage")-- created from saved doc and may or may not be altered


######### ONLY RUN BELOW ONCE #########

cite_dict= list()
cite_dict = [None] * len(citations)
x = 0
while x < len(citations):
    # our running dict list should be the right size for our current list of documents, coming from "citations" list
    cite_dict[x] = list()
    cite_dict[x] = [None] * len(citations[x])
    # label dicts for running dict list: which shooter
    cite_dict[x][0] = citations[x][0]
    y = 1
    while y < len(citations[x]):
        # set up dicts for running dict list
        cite_dict[x][y] = {}
        # label dicts for running dict list: which document
        dict_document_label = {'txt' : citations[x][y][0]}
        cite_dict[x][y].update(dict_document_label)
        y = y + 1
    x = x + 1

# basal format for our dictionary of approved/denied citations
f = open([insert desired filename for citation dictionary storage],'w')
f.write(str(cite_dict))
# you aren't going to be able to eval a blank document, so make sure you don't miss the above.

############# ONLY RUN ABOVE ONCE ########

# assuming we've already created the backup file of the dictionary of citations, load it.

if os.path.exists("/shooterdatalists/liststablesdocs/cite_dict_storage_current.txt"):
    with open("/shooterdatalists/liststablesdocs/cite_dict_storage_current.txt") as f:
        cite_dict_storage = literal_eval(f.read())

# create separate documents for "all citations" and "valid citations", for humans
# function walks you through sorting citations as in/valid

def sort(citations):
    f = open('[desired document 1-- yes and no]','w+')
    g = open('[desired document 2-- yes only]', 'w+')
    x = 0
    while x < len(citations):
        print "\n {}".format(citations[x][0])
        g.write(citations[x][0]+"\n \n")
        y = 1
        while y < len(citations[x]):
            if citations[x][y] == "adam lanza":
                pass
            else:
                print "{} \n".format(citations[x][y][0])
                g.write("\n \nshooter: " + citations[x][y][0]+"\n")
                z = 1
                while z < len(citations[x][y]):
                    did_i_update_doc = list()
                    # if this citation is already listed in the repository as valid/not valid, use that answer.
                    # we update the current running list "cite_dict", not the storage repository
                    this_ref = str(citations[x][y][z])
                    if this_ref in cite_dict_storage[x][y]:
                        g.write("\n" + "{}".format(citations[x][y][z]) + "\n")
                        # if the citation has not been evaluated, evaluate and save to both running dict list and storage repository
                    else:
                        print citations[x][y][z]
                        cite_truth = input("Is this citation legit? Enter 0 for no, 1 for yes, ctrl-C for break. \n")
                        cite_dict_storage[x][y].update({"{}".format(citations[x][y][z]) : cite_truth})
                        did_i_update_doc.append("yes")
                        print "\n"
                        z = z + 1
            if "yes" in did_i_update_doc:
                save_truth = input("\n Save changes for {} repository? 0 for no, 1 for yes. \n".format(citations[x][y][0]))
                if save_truth == 1:
                    f.write(str(cite_dict_storage))
                    g.write("\n")
                    g.write(str(citations[x][y][z-1]) + "\n")
            y = y + 1
        x = x + 1

sort(citations)

# check that there are no entries erroneously coded something other than 0 or 1

while x < len(cite_dict_storage):
    while y < len(cite_dict_storage[x]):
        for key,val in cite_dict_storage[x][y].items():
            if val == 0 or val == 1 or key == 'txt':
                pass
            else: print key
        y = y + 1
    x = x + 1

# what about misevaluated citations? right now, manual check only.

sort(citations)

# re-form the operating list of citations, amended to reflect the filtration we've done (valid only)

filt_cites_long = [None] * len(cite_dict_storage)
x = 0
# x corresponds to a shooter
while x < len(cite_dict_storage):
    # each shooter entry will need a subentry for every document
    filt_cites_long[x] = [None] * len(cite_dict_storage[x])
    # shooter name should be first element of shooter entry; this is the y = 0 for that x
    filt_cites_long[x][0] = cite_dict_storage[x][0]
    y = 1
    # y corresponds to a document for a fixed shooter
    while y < len(cite_dict_storage[x]):
        # why go the append route instead of the [None]*len() route? because we don't know how many entries were
        # marked valid vs invalid, so we don't know how much stuff we're going to be adding ahead of time
        filt_cites_long[x][y] = list()
        # document name
        filt_cites_long[x][y].append([val for key,val in cite_dict_storage[x][y].items() if key == "txt"][0])
        # this is the list of valid citations
        filt_cites_long[x][y].append([eval(key) for key,val in cite_dict_storage[x][y].items() if val == 1])
        y = y + 1
    # names without associated documents were screwing things up, so put a blank spot in anyway
    if len(cite_dict_storage[x]) == 1:
        filt_cites_long[x].append([])
    x = x + 1


# a list variation, sometimes another form more convenient: [...,[shooter, [all refs]],[shooter, [all refs]], ...]

filt_cites = list()
# same number of shooters -> same length
filt_cites = [None]*len(filt_cites_long)
x = 0
while x < len(filt_cites_long):
    # the 2 elements per entry will be shooter's name and list of outbound cites
    filt_cites[x] = [None] * 2
    filt_cites[x][1] = list()
    # first element of each entry should be shooter's name
    filt_cites[x][0] = filt_cites_long[x][0]
    # second element will be a list of all the outbound citations (see filt_cites_long to see why I'm using [1][1] )
    y = 1
    while y < len(filt_cites_long[x]):
        if len(filt_cites_long[x][y]) > 0:
            z = 0
            while z < len(filt_cites_long[x][y][1]):
                # x = shooter, y = document + cites, 1 = choose list of cites, z = specific citation, 0 = associated shooter
                filt_cites[x][1].append(filt_cites_long[x][y][1][z][0])
                z = z + 1
        y = y + 1
    x = x + 1

# list of unique citations (names only) grouped by shooter

citations_Unique = [None] * len(filt_cites)
x = 0
while x < len(filt_cites):
    citations_Unique[x] = []
    # every sublist has shooter name as first elements
    citations_Unique[x].append(filt_cites[x][0])
    # the rest of the sublist should be the alphabetized set of unique citations
    citations_Unique[x].append(sorted(set(filt_cites[x][1])))
    x = x + 1
