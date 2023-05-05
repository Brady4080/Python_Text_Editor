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
window.title("untitled")

""" Change Icon """
# Get the current working directory
cwd = os.getcwd()

# Construct the path to the icon file relative to the script location
icon_path = os.path.join(cwd, "icon.ico").replace("\\", "/")

# Capitalize the first letter of the drive letter (e.g. "c:/")
if len(icon_path) >= 2 and icon_path[1] == ":":
    icon_path = icon_path[0].upper() + icon_path[1:]
    
# Set the window icon using the relative file path
# window.iconbitmap(icon_path)

""" Fonts """
font1 = ['times', 12, 'normal']
font2 = ['arial', 12, 'normal']
currentFont = []

""" Line Numbers """ #FIXME: QOL
def getLineNum():
    output = ""
    row, col = input_field.index('end').split('.')
    for i in range(1, int(row)):
        output += str(i) + '\n'
    return output

def updateLineNum(event=None):
    lineNumBar = getLineNum()
    lineNum.config(state="normal")
    lineNum.delete(1.0, "end")
    lineNum.insert(1.0, lineNumBar)
    lineNum.tag_add("right", "1.0", "end")
    lineNum.config(state="disabled")

lineNum = tk.Text(
    window,
    width=5,
    padx=0,
    state="disabled",
    takefocus=0,
    background="light grey",
    wrap="none",
)
lineNum.pack(side="left", fill="y")
lineNum.tag_configure("right", justify="right")

"""" Text Box """
input_field = tk.Text(window, wrap="word", undo=True)
input_field.bind("<Configure>", updateLineNum)
input_field.bind("<KeyRelease>", updateLineNum)
input_field.pack(expand=True, fill="both")

""" Scroll Bar """ #FIXME: uniscrollbar
def sync_scrollbar(*args):
    input_field.yview(*args)
    lineNum.yview(*args)

scrollbar = tk.Scrollbar(window, command=sync_scrollbar)
scrollbar.pack(side="right", fill="y", before=input_field)

input_field.configure(yscrollcommand=scrollbar.set)
lineNum.configure(yscrollcommand=scrollbar.set)

""" Line Highlighting """


""" Menu Bar """
def todo():     # placeholder command (delete later)
    x = 0

menuBar = tk.Menu(window)


"""" file menu """
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
    fontsWindow = tk.Toplevel(window)
    fontsWindow.geometry("400x400")
    fontsWindow.title("Fonts")
    fontsWindow.resizable(False,False)

    """ Font Types """
    fontList = tk.Listbox(fontsWindow)
    fontScroll = tk.Scrollbar(fontsWindow)

    fontList.grid(row = 0, column = 0, columnspan = 3, sticky = tk.W, padx = 5, pady = 5)
    fontScroll.grid(row = 0, column = 3, columnspan = 1, sticky = tk.W+tk.NS, pady = 5)

    # Insert elements into the fontList
    fontList.insert(tk.END, "Times New Roman")
    fontList.insert(tk.END, "Arial")
    
    fontList.config(yscrollcommand = fontScroll.set)
    fontScroll.config(command = fontList.yview)

    """ Font Types """
    sizeList = tk.Listbox(fontsWindow)
    sizeScroll = tk.Scrollbar(fontsWindow)

    sizeList.grid(row = 0, column = 4, columnspan = 3, sticky = tk.W, padx = 5, pady = 5)
    sizeScroll.grid(row = 0, column = 7, columnspan = 1, sticky = tk.W+tk.NS, pady = 5)

    # Insert elements into the sizeList
    for size in range(8, 73):
        sizeList.insert(tk.END, size)

    sizeList.config(yscrollcommand = sizeScroll.set)
    sizeScroll.config(command = sizeList.yview)

    """  """
    fontOkay = tk.Button(fontsWindow, text = "Okay", command = 'todo')
    fontCancel = tk.Button(fontsWindow, text = "Cancel", command = 'todo')
    fontOkay.grid(row = 1, column = 4, columnspan = 2, sticky = tk.W, padx = 5, pady = 5)
    fontCancel.grid(row = 1, column = 6, columnspan = 2, sticky = tk.W, padx = 5, pady = 5)



formatMenu = tk.Menu(menuBar, tearoff=0)
formatMenu.add_command(label="Font", command=lambda:fontAct())

menuBar.add_cascade(label="Format", menu=formatMenu)    # add formatMenu to menuBar


""" viewMenu Functions """
def zoomAct(str1):
    if(str1=='zoomIn'):
        font1[1]=font1[1]+2
    else:
        font1[1]=font1[1]-2
    input_field.config(font=font1)

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

window.mainloop() #calling the gui window