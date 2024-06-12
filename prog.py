import tkinter as tk
from tkinter import filedialog

file_address = ""
upper_form = ""

def open_file():
    global file_address
    global list_form
    file_address = filedialog.askopenfile(initialdir="/codes/oop", title="Select a file", filetypes=(("Text files", "*.txt"),("All files", "*.*")))
    if file_address: file_address = file_address.name
    read_file = open(f"{file_address}", "r")
    list_form = read_file.readlines()
    label.config(text=f"{''.join(list_form)}")
    read_file.close()

def upper_file():
    global list_form
    global new_list
    new_list = []
    read_file = open(f"{file_address}", "r")
    list_form = read_file.readlines()
    for element in range(len(list_form)):
        global upper_form
        upper_form = list_form[element].upper()
        new_list.append(upper_form)
    label.config(text=f"{''.join(new_list)}")
    read_file.close()

def save_file():
    write_file = open(f"{file_address}", "w")
    for element in range(len(list_form)):
        write_file.write(new_list[element])
    write_file.close()
    label.config(text="File saved.")

def help_option():
    label.config(text='''All the menu selections are at the top. In the File menu,\n
                 Open option will let you open and select a file (text file is recommended to be used).\n
                 The Save option will edit the file selected. The Quit option will close the app.\n
                 In the Edit menu, Convert to upper option will make\nall the contents of the file turn to uppercase.''')
    
def about_option():
    label.config(text='''This app is intended to be used to edit files,\n
                 specifically to turn uppercase the contents of the selected file.\n
                 This app can access files and edit the contents of the file using python programming.''')

main_window = tk.Tk()
main_window.title("File Editor")
main_window.geometry("600x500")

main_frame = tk.Frame(main_window)
main_frame.pack(fill="both", expand=True)

label = tk.Label(main_frame, text=upper_form)
label.pack(fill="both", expand=True)

main_menu = tk.Menu(main_window)
main_window.config(menu=main_menu)

file_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command= open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Quit", command=exit)

help_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=help_option)
help_menu.add_command(label="About", command=about_option)

edit_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Convert to upper", command=upper_file)

main_window.mainloop()