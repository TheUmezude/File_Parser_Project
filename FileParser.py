import tkinter as tk
from tkinter import filedialog, Text
import GUI_tkinter
from tkinter import *
import os # To enable you walk through the OS directory
import re # To enable pattern recognition

inner_container = []  # Going to use a list, instead of normal variable for future modification


# Define functionality for buttons
def parse_folder():
    for widget in GUI_tkinter.app_frame.winfo_children():
        widget.destroy()

    global inner_container
    inner_container = []
    folder_path = filedialog.askdirectory(initialdir="/", title="Select Folder")
    inner_container.append(folder_path)

    for items in inner_container:
        print_text = f"The selected folder path is: {items}"
        label = tk.Label(GUI_tkinter.app_frame, text=print_text, background="yellow")
        label.pack()


def find_stuff():
    # Take file-path and extract names of files in file-path as list data type
    check_folder = inner_container[0]
    found_items = os.listdir(check_folder)

    # Initialize what the pattern to be searched for should look like
    pattern = "\W\W\W"

    # Look into the individual txt files and extraxt the description
    for items in range(0, len(found_items)):
        prompt_1 = f"\n({items + 1}): I found the file named: {found_items[items]}"
        label_1 = tk.Label(GUI_tkinter.app_frame, text=prompt_1, background="white")
        label_1.pack()
        inside_file = check_folder + '\\' + found_items[items]

        with open(inside_file, mode='r', encoding='utf-8') as myfile:
            prompt_2 = "Inside the file, I found this description: \n "
            label_2 = tk.Label(GUI_tkinter.app_frame, text=prompt_2, background="white")
            label_2.pack()
            contents = myfile.readlines()

            for indexing in range(0, len(contents)):
                if re.search(pattern, contents[indexing]):
                    content_1 = contents[indexing + 1]
                    label_3 = tk.Label(GUI_tkinter.app_frame, text=content_1, background="white")
                    label_3.pack()
                    break

            print("\n\n")