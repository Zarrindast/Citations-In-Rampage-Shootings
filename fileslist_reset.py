# the fileslist list has been known to go bonkers due to user error (ahem)... run this subsequent to the use of scraping_Langman.py

fileslist = list()
fileslist = [None] * len(names_Docs_Grouped)
x = 0
while x < len(names_Docs_Grouped):
    fileslist[x] = list()
    fileslist[x] = [None] * len(names_Docs_Grouped[x])
    fileslist[x][0].append(names_Docs_Grouped[x][0])
    y = 1
    while y < len(names_Docs_Grouped[x]):
        if "pdf" not in names_Docs_Grouped[x][y].lower():
            print "names_Docs_Grouped[{},{}] is not a pdf, see url below:".format(x,y); print(names_Docs_Grouped[x][y])
            del names_Docs_Grouped[x][y]
        else:
            fileslist[x].append(str(names_Docs_Grouped[x][y][cutoff:]))
        y = y + 1
    x = x + 1
