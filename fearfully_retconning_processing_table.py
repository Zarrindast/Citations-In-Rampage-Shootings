# a little late, but a table, "processing_table" of the status quo,
# which will be exported to CSV so it can be manually updated as I inspect the tesseracted files:

# quality of file yielded by attempting OCR with PDF2TXT on original pdf
processing_table["P2Tfile"] = ""
# what remained to be done at that point
processing_table["stat_after_P2T"] = ""
# quality of file yielded by tesseracting original pdf (needs to be updated manually per file inspected)
processing_table["tessfile"] = ""
# what remained to be done at that point (pending until file inspections done; then contingent on above)
processing_table["stat_after_tess"] = ""
# whether any handwriting element needs to be transcribed
processing_table["handwritten"] = ""
# anything else I need to note
processing_table["notes"] = ""
# when "do" was made, it was just my list of things left to do after I tried P2T, so this can be renamed
## code cleanup note: RENAMED and placed appropriately among other columns, not just copied w/ a new name please
## code cleanup note: though otoh I may wish to retain a copy of "do" here to reference easily in case something goes awry
## code cleanup note: as long as I can remember what it even meant with such a vague name, which is the whole reason I was changing it
processing_table["stat_after_P2T"] = processing_table["do"]
x = 0
# working backwards (and fwds) to fill out the table of my steps.
## code cleanup note: consider commenting this out more?
while x < len(processing_table):
    # if I marked it for OCR after P2T, the P2T file was bad and the tess result remains to be seen
    if 'OCR' in processing_table["stat_after_P2T"][x]:
        processing_table["P2Tfile"][x] = 'bad'
        processing_table["tessfile"][x] = 'pending'
        processing_table["stat_after_tess"][x] = 'pending'
    # if it WASN'T marked for OCR, I didn't tess it and nothing has changed between finishing P2T and now
    else:
        processing_table["tessfile"][x] = 'DNE'
        processing_table["stat_after_tess"][x] = str(processing_table["stat_after_P2T"][x])
    # did I find something usable in my P2T file? and am I done (* marked) or was it only partial (* and something else)?
    if '*' in processing_table["stat_after_P2T"][x]:
        processing_table["P2Tfile"][x] = 'usable'
    # was there handwriting, and was that all?
    # for items that were partially H, add H in there
    if 'H' in processing_table["stat_after_P2T"][x]:
        processing_table["stat_after_tess"][x] += 'H'
        # added this later, check if something goes wrong
        processing_table["handwritten"][x] = "y"
    # correction of double "H" addition to some items
    if processing_table["stat_after_P2T"][x] == 'H':
        processing_table["P2Tfile"][x] = 'DNE'
        processing_table["stat_after_tess"][x] = 'H'
    # rows that are merely names of shooters don't have any associated documents.
    if "-" in processing_table["do"][x]:
        processing_table["P2Tfile"][x] = 'DNE'
    # something was thrown out, the P2T may as well not exist. the tess side of the chart was already taken care of
    # in the "no" case for OCR marking
    if processing_table["do"][x] == 'X':
        processing_table["P2Tfile"][x] = 'DNE'
    x = x + 1

proc_table_old = processing_table
processing_table = processing_table.drop(["do"], axis = 1)

# export all this to a CSV...
folder = "/shooterdatalists/origdocs"
processing_table.to_csv(r"{}/file_processing_table".format(folder))
# the "r" is supposed to be there to prevent a unicode reading error

#
# It was easier to manually open (or preview), inspect, and classify by eye each document than to write a script to open each 
# document for me and prompt me for a classification, though I may come back and do so if I decide to
# polish things up after the actual goal is accomplished. A factor to conisder is the automatic
# opening of very, very large documents being a danger to my RAM.
