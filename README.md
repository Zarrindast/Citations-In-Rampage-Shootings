# Citations In Rampage Shootings

This project identifies citation networks within rampage shooting incidents. 

In the end, we produce a directed acyclic graph. Each node is: one shooter together with all of their associated documents, which include manifestos, transcriptions of videos, spreadsheets kept by shooters, police documentation of possessions, etc (being careful to exclude mentions of other incidents that are NOT originating from the shooter themself and do NOT concretely indicate that that shooter was exposed to the previous incident). Each edge is a mention/citation.

First, it is necessary to scrape the web for documents associated with the shooters. These could be in many forms. Initially I'm going to do just rampage shooters that are in Peter Langman's database on his site.

Then, everything has to be converted into txt form, which involves several iterations of OCR, audio-to-text technology and direct transcription, etc.  

All txt files are then searched for references to other incidents/shooters, including such keywords as the first and/or last names of the shooters as well as nicknames; names of the schools where the crimes took place; slang relating to previous incidents (such as may have cropped up in the true crime community online after an incident, e.g. "Holmies" for James Holmes); titles of or content inside others' manifestos, etc. These citations are catalogued by occurence, content, and location. 

False positive citations are manually fished out

The graph is created and visualized.

After that initial model is up, I'll try to flesh out all of the metions that aren't of shooters already on the list (with the possible exception of Adam Lanza's comprehensive spreadsheet, at least for now).


ORDER OF EVENTS
	scraping_Langman.py (creates shooterpages.txt)
    dependencies: pkgs listed internally
	
first_pdf_to_text_attempt.py
    dependencies: pkgs listed internally, scraping_Langman.py

tesseracting_whatsleft.py
    dependencies: pkgs listed internally, scrapinglangman.py, first_pdf_to_text_attempt.py, multipage_ocr.py

fearfully_retconning_processing_table.py (creates file_processing_table.csv)
    dependencies: pkgs listed internally, scrapinglangman.py, first_pdf_to_text_attempt.py, multipage_ocr.py,           tesseracting_whatsleft.py


 	Add files via upload 	5 days ago
	
