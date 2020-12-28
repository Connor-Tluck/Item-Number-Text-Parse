import re
import tkinter as tk
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()

#user select the text file to process
text_file = filedialog.askopenfilename()
File_object = open(text_file,"r")
contents = File_object.read()

def find_item_numbers(file):
    items_found = re.findall(r'ITEM \d+.\d+',file.upper())
    return(sorted(set(items_found)))

items_set = find_item_numbers(contents)

print(items_set)

with open('items_found.txt', 'w') as filehandle:
    for listitem in items_set:
        filehandle.write('%s\n' % listitem)
