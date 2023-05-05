import tkinter as tk
from gui.line_numbers import *

def createTextBox(window):
    input_field = tk.Text(window, wrap="none", undo=True)
    input_field.pack(expand=True, fill="both")
    
    # Add a tag for highlighting the current line
    input_field.tag_configure("current_line", background="#FFFFCC")
    
    def updateLineHighlight(event=None):
        # Remove highlighting from the previous current line
        input_field.tag_remove("current_line", "1.0", "end")
        # Add highlighting to the new current line
        input_field.tag_add("current_line", "insert linestart", "insert lineend+1c")
        
    # Bind the updateLineHighlight function to the appropriate events
    input_field.bind("<Key>", updateLineHighlight)
    input_field.bind("<Button-1>", updateLineHighlight)
    input_field.bind("<Button-3>", updateLineHighlight)
    input_field.bind("<MouseWheel>", updateLineHighlight)
    input_field.bind("<Return>", updateLineHighlight)
    
    return input_field

def increaseLineNum(input_field, lineNum):
    def delayedUpdateLineNum(event):
        input_field.after(1, updateLineNum, lineNum, input_field)
    input_field.bind("<Configure>", lambda event: updateLineNum(lineNum, input_field))
    input_field.bind("<Return>", delayedUpdateLineNum)

def decreaseLineNum(input_field, lineNum):
    def delayedUpdateLineNum(event):
        input_field.after(1, updateLineNum, lineNum, input_field)
    input_field.bind("<Configure>", lambda event: updateLineNum(lineNum, input_field))
    input_field.bind("<KeyRelease>", lambda event: delayedUpdateLineNum(event))
