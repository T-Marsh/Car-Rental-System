import tkinter as tk
from tkinter import messagebox

from staff_gui import StaffGUI

class RCBSGUI():

    def __init__(self):   

        print("Creating RCBS GUI ...")

        self.current_gui = None # Reference to current GUI 

        self.root = tk.Tk()
        self.root.title("Rental Car Booking System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinates (width, height, x, y) :", 
              width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)

        # Add menu items
        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="File", menu=filemenu)
       
        # Staff menu (pulldown)
        # Create a pulldown menu
        staff_menu = tk.Menu(menubar, tearoff=0)
        # Add menu items
        # do not use self.create_staff_gui()
        staff_menu.add_command(label="Staff", 
            command=self.create_staff_gui) 
        # Add pulldown menu to toplevel menu
        menubar.add_cascade(label="Staff", menu=staff_menu)

        # Display the menu
        self.root.config(menu=menubar)

        pass
            
    # Functions to create child frames 
    # when menu options are selected

    def create_staff_gui(self):
        pass

if __name__ == '__main__':
    gui = RCBSGUI()
    gui.root.mainloop()
    pass        