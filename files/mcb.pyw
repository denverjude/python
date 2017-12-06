#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboad
# USAGE: mcb.pyw save <keyword> - Saves clipboard to keybword.
#        mcb.pyw load <keyword> - Loads keybword to clipboard.
#        mcb.pyw list- Loads all keywords to clipboard
#        mcb.pyw delete <keyword> - Deletes keyword
#        mcb.pyw delete- Deletes all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# todo: Save clipboard content. Check len(sys.argv) == 3 because save can also be a keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'load':
    if sys.argv[2] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[2]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    for i in mcbShelf:
        del mcbShelf[i]
# todo: List keywords and load content
    
        
    


mcbShelf.close()


