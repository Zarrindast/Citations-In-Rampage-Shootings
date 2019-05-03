# at this point I realized I had some very inconvenient artifacts left over from
# web scraping: everyone's name having a hyphen in it, an arbitary "0" on someone's name...
# moreover I needed to get rid of suffixes, since they will only hinder reference searches.
nameslist_Search = copy.deepcopy(nameslist)
nameslist_Search = [s.replace("-"," ") for s in nameslist_Search]

x = 0
while x < len(nameslist_Search):
    # remove all hyphens, "real" and "unreal", in files list to search
    fileslist_ready[x][0] = fileslist_ready[x][0].replace("-"," ")
    # kill suffixes in all our lists. yes, I should have done this before the names propogated.
    for suffix in [" jr", " jr.", " sr", " sr.", " 0"]:
        if suffix in nameslist_Search[x]:
            print "{}; {}".format(nameslist_Search[x], suffix)
            nameslist_Search[x] = nameslist_Search[x][:-len(suffix)]
    x = x + 1

# I applied the same changes to my folders en masse using the OSX GUI.

# we're gonna replace names to search with lists of names (ie nicknames, misspellings, etc) per person
namesearch_Long = [None] * len(nameslist_Search)
x = 0
while x < len(nameslist_Search):
    namesearch_Long[x] = []
    namesearch_Long[x].append(nameslist_Search[x])
    x = x + 1

# going to be splitting up the names through multiple methods to achieve all possible
# ways the correctly spelled name could be referenced, but don't want duplicates, so:
def uniquelistadd(oldlist, newlist):
    for elm in newlist:
        if elm not in oldlist:
            oldlist.append(elm)
    print oldlist

x = 0
while x < len(nameslist_Search):
    #'chris harper mercer' -> 'chris','harper mercer'
    uniquelistadd(namesearch_Long[x],nameslist_Search[x].split(" ",1))
    # 'seung hui cho' -> 'seung hui','cho'
    uniquelistadd(namesearch_Long[x],nameslist_Search[x].rsplit(" ",1))
    x = x + 1
