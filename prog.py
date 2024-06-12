import tkinter as tk
from tkinter import filedialog

file = ""

def open_file():
    global file
    file = filedialog.askopenfile(initialdir="/codes/oop", title="Select a file", filetypes=(("Text files", "*.txt"),("All files", "*.*")))
    print(file.name)

def file_section():
    menu_selection = tk.LabelFrame(main_frame)
    menu_selection.grid(column=0, row=0, sticky="news")

    open_button = tk.Button(menu_selection, text="Open", command=open_file)
    open_button.grid(column=0, row=0)

    save_button = tk.Button(menu_selection, text="Save",)
    save_button.grid(column=0, row=1)

    quit_button = tk.Button(menu_selection, text="Quit", command=exit)
    quit_button.grid(column=0, row=2)

main_window = tk.Tk()
main_window.title("File Editor")
main_window.geometry("500x500")

main_frame = tk.Frame(main_window)
main_frame.pack(fill="both", expand=True)

menu_frame = tk.LabelFrame(main_frame)
menu_frame.pack(side="top", fill="x")

file_button = tk.Button(menu_frame, text="File", command=file_section)
file_button.pack(side="left")

help_button = tk.Button(menu_frame, text="Help")
help_button.pack(side="left")

main_window.mainloop()