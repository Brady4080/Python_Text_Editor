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
from tkinter import *

"""" Main Gui """
window = Tk()
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

""""Temp Icon REMOVE LATER"""
window.iconbitmap("C:/Users/Brady/Desktop/Python-Text-Editor/icon.ico") #temp

"""" Text Box """
input_field = Text(window, bg=window["background"], width=150, height=200)
input_field.pack(fill = BOTH, expand = True)



""" Menu Bar """
def todo():
    x = 0

menuBar = Menu(window)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=todo)
fileMenu.add_command(label="Open", command=todo)
fileMenu.add_command(label="Save", command=todo)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.destroy)

menuBar.add_cascade(label="File", menu=fileMenu)


editMenu = Menu(menuBar, tearoff=0)
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

menuBar.add_cascade(label="Edit", menu=editMenu)


formatMenu = Menu(menuBar, tearoff=0)
formatMenu.add_command(label="Font", command=todo)
menuBar.add_cascade(label="Format", menu=formatMenu)


viewMenu = Menu(menuBar, tearoff=0)
subMenuView = Menu(viewMenu, tearoff=0)
subMenuView.add_command(label='Zoom In')
subMenuView.add_command(label='Zoom Out')

viewMenu.add_cascade(label="Zoom", menu=subMenuView)
menuBar.add_cascade(label="View", menu=viewMenu)


helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Help Index", command=todo)
helpMenu.add_separator()
helpMenu.add_command(label="About", command=todo)

menuBar.add_cascade(label="Help", menu=helpMenu)

window.config(menu=menuBar)




window.mainloop() #calling the gui window