# at this point I realized I had some very inconvenient artifacts left over from
# web scraping: everyone's name having a hyphen in it, an arbitary "0" on someone's name...
# moreover I needed to get rid of suffixes, since they will only hinder reference searches.
nameslist_Search = copy.deepcopy(nameslist)
nameslist_Search = [s.replace("-"," ") for s in nameslist_Search]

x = 0
while x < len(nameslist_Search):
    # remove all hyphens, "real" and "unreal", in files list to search
    fileslist_ready[x][0] = fileslist_ready[x][0].replace("-"," ")
    fileslist_ready[x][0] = fileslist_ready[x][0].replace(" 0","")
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

writelistoflists(namesearch_Long,"namesearch_Long_orig.txt")

#import json
#os.chdir("/shooterdatalists")
#with open("namesearch_Long_orig.txt", "w+") as f:
#    json.dump(namesearch_Long, f)

# this isn't working. cut and paste for now:
#with open("namesearch_Long.txt", "r") as f:
#    namesearch_Long = json.load(f)

namesearch_Long = []
namesearch_Long = [[u"william atchison", u"atchison"],[u"pekka eric auvinen", u"pekka", u"eric auvinen", u"pekka eric", u"pekka-eric", u"auvinen", u"jokela", u"tuusula", u"humanity is overrated", u"naturalselector89"], [u"kenneth bartley", u"campbell county"], [u"amy bishop", u"bishop"], [u"bastian bosse", u"sebastian", u"bastian", u"bosse", u"emsdetten", u"geschwister"], [u"sky bouche", u"bouche", u"forest high"], [u"nathaniel brazill", u"nathaniel brazil", u"nathanial brazil", u"nathanial brazill", u"brazill"], [u"robert butler", u"butler jr", u"millard south"], [u"michael carneal", u"carneal"], [u"alvaro castillo", u"alvaro", u"castillo", u"orange high school"], [u"douglas chanthabouly", u"chanthabouly", u"henry foss", u"foss", u"tacoma"], [u"seung hui cho", u"s.h. cho", u"seung", u"v-tech", u"v. tech", u"v tech", u"vtech", u"virginia tech"], [u"nikolas cruz", u"nikolas", u"cruz", u"nicholas cruz"], [u"wellington de oliveira", u"wellington", u"oliveira"], [u"dorothy dutiel", u"dutiel"], [u"bruco eastwood", u"bruco", u"eastwood"], [u"valery fabrikant", u"valery", u"fabrikant"], [u"robert flores"], [u"jaylen fryberg", u"jaylen", u"fryberg"], [u"kimveer gill", u"kimveer", u"gill"], [u"robert gladden", u"gladden"], [u"one goh"], [u"drew golden", u"golden", u"drew & mitchel", u"drew and mitchel"], [u"mitchell johnson", u"mitchel", u"golden & johnson", u"golden and johnson"], [u"eric hainstock", u"hainstock"], [u"biswanath halder", u"biswanath", u"halder"], [u"james hancock", u"hancock"], [u"kristofer hans", u"kristofer"], [u"chris harper", u"christopher harper", u"harper mercer", u"harper-mercer"], [u"eric harris", u"eric", u"april 20", u"harris", u"reb", u"arlene", u"columbine", u"nbk", u"wrath", u"godlike", u"natural born killer", u"naturalselect", u"natural select", u"littleton", u"dylan klebold", u"dylan kleibold", u"dylan", u"klebold", u"vodka", u"zero day", u"zero hour"], [u"james holmes", u"holmes", u"holmie", u"joker", u"batman", u"theater shooting", u"dark knight", u"aurora"], [u"eric houston", u"houston"], [u"alex hribal", u"hribal"], [u"james kearbey", u"kearbey"], [u"leo kelly"], [u"su yong kim", u"su-yong", u"yong kim", u"su yong"], [u"kip kinkel", u"kip", u"kipland", u"kinkel", u"kinkle"], [u"tj lane", u"tj lang", u"thomas michael lane", u"t.j."], [u"adam lanza", u"lanza", u"sandy hook"], [u"keith ledeger", u"ledeger"], [u"steven leith", u"leith"], [u"marc l%C3%A9pine", u"l%C3%A9pine", u"mark lepine", u"lepine", u"mark l%C3%A9pine", u"polytechnique"], [u"patrick lizotte", u"lizotte", u"valley high school"], [u"wayne lo", u"bard college"], [u"jared loughner", u"jared lee", u"loughner", u"tuscon", u"giffords"], [u"barry loukaitis", u"loukaitis", u"frontier middle school", u"moses lake"], [u"kelvin love", u"kelvin ray love", u"garland community college"], [u"gang lu", u"university of iowa"], [u"myron may", u"myron", u"myron de'shawn may"], [u"odane maye", u"odane", u"odane greg maye", u"hampton university"], [u"john mclaughlin", u"mclaughlin", u"rocori", u"cold spring"], [u"david moore", u"noblesville"], [u"stephen morgan", u"wesleyan"], [u"duane morrison", u"platte canyon"], [u"peter odighizuwa", u"odighizuwa", u"appalachian"], [u"bryan oliver", u"taft union"], [u"jesse osborne", u"townville"], [u"brendan orourke", u"orourke", u"o'rourke", u"kelly elementary"], [u"jared padgett", u"padgett", u"reynolds"], [u"dimitrios pagourtzis", u"dimitrios", u"pagourtzis", u"santa fe"], [u"gabriel parker", u"gabriel", u"parker"], [u"karl pierson", u"pierson"], [u"evan ramsey", u"bethel regional"], [u"jose reyes", u"jose h. reyes", u"jose h reyes", u"sparks middle school"], [u"elliot rodger", u"eliot rodger", u"elliot roger", u"eliot roger", u"supreme gentleman", u"magnificent", u"ultimate gentleman", u"isla vista", u"incel"], [u"jon romano", u"columbia high school"], [u"jamie rouse", u"richland high"], [u"jonathan rowan", u"university of washington"], [u"matti saari", u"matti", u"saari", u"kauhajoki"], [u"ely serna", u"west liberty salem"], [u"caleb sharpe", u"freeman high"], [u"michael slobodian", u"slobodian", u"brampton centennial"], [u"brenda spencer", u"brenda", u"spencer", u"grover cleveland elementary"], [u"randy stair", u"andrew blaze", u"tranny phantom", u"danny phantom", u"mackenzie west", u"weis market", u"E.G.S"], [u"nicco tatum", u"nicco", u"tatum"], [u"jeffrey weise", u"jeff weise", u"geoffery weise", u"geoff weise", u"red lake"], [u"charles whitman", u"university of texas", u"tower shooting", u"Texas sniper"], [u"andy williams", u"charles andrew williams", u"andrew williams", u"charles williams", u"satana high", u"santee"], [u"james wilson", u"oakland elementary"], [u"jiverly wong", u"jiverly", u"binghamton"], [u"luke woodham", u"woodham", u"pearl high school"], [u"aaron ybarra", u"ybarra", u"seattle pacific", "S.P.U."], [u"john zawahri", u"zawahri", u"santa monica"], [u"haiyang zhu", u"haiyang", u"zhu"]]
