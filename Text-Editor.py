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

