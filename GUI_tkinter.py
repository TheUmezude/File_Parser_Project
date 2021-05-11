from FileParser import *
from FileParser import parse_folder, find_stuff
# Note that the methods in the tkinter library start with capital letters.

# Set up the GUI
root = tk.Tk()

# To adjust the size an properties of the generated tkinter canvas.
app_canvas = tk.Canvas(root, height=600, width=600, background='dark green')
app_canvas.pack() # To attach the canvas to the interface.

app_frame = tk.Frame(root, background='white') # To make a frame inside the canvas
app_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) # Tweaking the dimensions of the frame

# Create text widget and specify size.
# T = Text(app_frame, height=5, width=52) -- For creating writing boxes
# T.pack(side=TOP)

# Create label
intro_label = Label(app_frame, text="Select the folder you wish to analyze. \n Click 'Analyze'", foreground="dark green")
intro_label.config(font=("Courier", 14))
intro_label.pack()


# Adding Buttons to the GUI
open_folder = tk.Button(root, text="Select Folder", padx=10, pady=5, foreground="white", background="dark green",
                        command=parse_folder) # Note that button can be attached to root or frame
open_folder.pack(side=LEFT)

analyze = tk.Button(root, text="Analyze", padx=10, pady=5, foreground="white", background="dark green",
                    command=find_stuff)
analyze.pack(side=RIGHT)
