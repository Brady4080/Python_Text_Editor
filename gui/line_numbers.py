import tkinter as tk

def getLineNum(input_field):
    output = ""
    row, col = input_field.index('end').split('.')
    for i in range(1, int(row)):
        output += str(i) + '\n'
    return output

def updateLineNum(lineNum, input_field):
    lineNumBar = getLineNum(input_field)
    lineNum.config(state="normal")
    lineNum.delete(1.0, "end")
    lineNum.insert(1.0, lineNumBar)
    lineNum.tag_add("right", "1.0", "end")
    lineNum.config(state="disabled")

def createLineNumBar(window):
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
    return lineNum
