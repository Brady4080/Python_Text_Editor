import tkinter as tk
from gui import line_numbers, text_box, menu
#import file_menu

window = tk.Tk()
window.config(background="white")
window.geometry("1280x720")
window.title("untitled")

lineNum = line_numbers.createLineNumBar(window)
input_field = text_box.createTextBox(window)
increaseLineNum = text_box.increaseLineNum(input_field, lineNum)
decreaseLineNum = text_box.decreaseLineNum(input_field, lineNum)


#file_menu = create_file_menu(window)
menus_menu = menu.menus_create_menu(window)

window.mainloop()
