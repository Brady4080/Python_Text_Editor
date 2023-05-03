# A text editor made in python
# 
#                      Text Widget
# T = Text(root, bg, fg, bd, height, width, font, ..)
# root – root window. 
# bg – background colour 
# fg – foreground colour 
# bd – border of widget. 
# height – height of the widget. 
# width – width of the widget. 
# font – Font type of the text. 
# cursor – The type of the cursor to be used. 
# insetofftime – The time in milliseconds for which the cursor blink is off. 
# insertontime – the time in milliseconds for which the cursor blink is on.  
# padx – horizontal padding. 
# pady – vertical padding. 
# state – defines if the widget will be responsive to mouse or keyboards movements. 
# highlightthickness – defines the thickness of the focus highlight. 
# insertionwidth – defines the width of insertion character. 
# relief – type of the border which can be SUNKEN, RAISED, GROOVE and RIDGE. 
# yscrollcommand – to make the widget vertically scrollable. 
# xscrollcommand – to make the widget horizontally scrollable. 
#
#               Some Common methods
# index(index) – To get the specified index. 
# insert(index) – To insert a string at a specified index. 
# see(index) – Checks if a string is visible or not at a given index. 
# get(startindex, endindex) – to get characters within a given range. 
# delete(startindex, endindex) – deletes characters within specified range.
#
#               Tag handling methods 
# tag_delete(tagname) – To delete a given tag. 
# tag_add(tagname, startindex, endindex) – to tag the string in the specified range 
# tag_remove(tagname, startindex, endindex) – to remove a tag from specified range 
#
#               Mark handling methods 
# mark_names() – to get all the marks in the given range. 
# index(mark) – to get index of a mark. 
# mark_gravity() – to get the gravity of a given mark.

import os
import tkinter as tk

"""" Main Gui """
window = tk.Tk()
window.config(background="white")
window.geometry("1280x720")

""" Change Icon """

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Get the current working directory
cwd = os.getcwd()

# Construct the path to the icon file relative to the script location
icon_path = os.path.join(cwd, "icon.ico").replace("\\", "/")

# Capitalize the first letter of the drive letter (e.g. "c:/")
if len(icon_path) >= 2 and icon_path[1] == ":":
    icon_path = icon_path[0].upper() + icon_path[1:]
    
# Set the window icon using the relative file path
####### window.iconbitmap(icon_path) #######
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""" TODO Temp Icon REMOVE LATER"""
window.iconbitmap("C:/Users/Brady/Desktop/Python-Text-Editor/icon.ico") #temp

""" Fonts """
font1=['times', 12, 'normal']
font2=['arial', 12, 'normal']
currentFont = []

"""" Text Box """
# makes a new line when the enter key is pressed
def insert_newline(event):
    input_field.insert(tk.INSERT, "\n")
    return 'break'

input_field = tk.Text(window, wrap="none")
input_field.pack(fill = "both", expand = True, padx=15)
input_field.bind("<Return>", insert_newline)


""" Menu Bar """
def todo():     # placeholder command (delete later)
    x = 0

menuBar = tk.Menu(window)
fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=todo)
fileMenu.add_command(label="Open", command=todo)
fileMenu.add_command(label="Save", command=todo)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.destroy)

menuBar.add_cascade(label="File", menu=fileMenu)        # add fileMenu to menuBar


editMenu = tk.Menu(menuBar, tearoff=0)
editMenu.add_command(label="Select All", command=todo)
editMenu.add_separator()
editMenu.add_command(label="Copy", command=todo)
editMenu.add_command(label="Paste", command=todo)
editMenu.add_command(label="Cut", command=todo)
editMenu.add_command(label="Delete", command=todo)
editMenu.add_separator()
editMenu.add_command(label="Find...", command=todo)
editMenu.add_command(label="Go To...", command=todo)
editMenu.add_command(label="Replace...", command=todo)

menuBar.add_cascade(label="Edit", menu=editMenu)        # add editMenu to menuBar


""" formatMenu Functions """
def fontAct():
    'todo'

formatMenu = tk.Menu(menuBar, tearoff=0)
formatMenu.add_command(label="Font", command=lambda:fontAct())

menuBar.add_cascade(label="Format", menu=formatMenu)    # add formatMenu to menuBar


""" viewMenu Functions """
def zoomAct(str1):
    if(str1=='zoomIn'):
        currentFont[1]=currentFont[1]+2
    else:
        currentFont[1]=currentFont[1]-2
    input_field.config(font=currentFont)

viewMenu = tk.Menu(menuBar, tearoff=0)
zoomSubMenu = tk.Menu(viewMenu, tearoff=0)
zoomSubMenu.add_command(label='Zoom In', command=lambda:zoomAct('zoomIn'))
zoomSubMenu.add_command(label='Zoom Out', command=lambda:zoomAct(''))

viewMenu.add_cascade(label="Zoom", menu=zoomSubMenu)    # add zoomSubMenu to viewMenu
menuBar.add_cascade(label="View", menu=viewMenu)        # add viewMenu to menuBar


helpMenu = tk.Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help Index", command=todo)
helpMenu.add_separator()
helpMenu.add_command(label="About", command=todo)

menuBar.add_cascade(label="Help", menu=helpMenu)        # add helpMenu to menuBar

window.config(menu=menuBar)

""" Scroll Bar """ #FIXME: fix the inverse scrollbar
scrollbar = tk.Scrollbar(window, command=input_field.yview)
scrollbar.pack(side="right", fill="y", before=input_field)
input_field.configure(yscrollcommand=scrollbar.set)

""" Line Numbers """ #FIXME: update the location and how the output
# create the line number label
line_number = tk.Label(window, width=1, highlightthickness=0, borderwidth=0)
line_number.pack(side="left", fill="y")

def update_line_numbers(event=None):
    line_number_text = ""
    line, column = map(int, input_field.index("end-1c").split("."))
    for i in range(1, line+1):
        line_number_text += str(i) + "\n"
    line_number.config(text=line_number_text)

# initial line numbers
update_line_numbers()

# position the line number label on the left side
line_number.place(relx=0.0, rely=0.0, relheight=1.0)

# bind the update_line_numbers function to the Configure and KeyRelease events
input_field.bind("<Configure>", update_line_numbers)
input_field.bind("<KeyRelease>", update_line_numbers)
input_field.bind("<MouseWheel>", update_line_numbers)

""" Line Highlighting """


window.mainloop() #calling the gui window