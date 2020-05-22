import tkinter as tk
from tkinter import messagebox

from staff_gui import StaffGUI
from customer_gui import CustomerGUI
# from car_gui import CarGUI
# from booking_gui import BookingGUI
# from invoice_gui import InvoiceGUI

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

        # Quit Program menu
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Program", menu=filemenu)
       
        # Staff menu (pulldown)
        staff_menu = tk.Menu(menubar, tearoff=0)
        staff_menu.add_command(label="Staff", 
            command=self.create_staff_gui)
        menubar.add_cascade(label="Staff", menu=staff_menu)

        # Customer menu (pulldown)
        customer_menu = tk.Menu(menubar, tearoff=0)
        customer_menu.add_command(label="Customer", 
            command=self.create_customer_gui)
        menubar.add_cascade(label="Customer", menu=customer_menu)

        # Car menu (pulldown)
        car_menu = tk.Menu(menubar, tearoff=0)
        # car_menu.add_command(label="Car", 
            # command=self.create_car_gui)
        menubar.add_cascade(label="Car", menu=car_menu)

        # Booking menu (pulldown)
        booking_menu = tk.Menu(menubar, tearoff=0)
        # booking_menu.add_command(label="Booking", 
        #     command=self.create_booking_gui)
        menubar.add_cascade(label="Booking", menu=booking_menu)

        # Invoice menu (pulldown)
        invoice_menu = tk.Menu(menubar, tearoff=0)
        # Invoice_menu.add_command(label="Invoice", 
        #     command=self.create_Invoice_gui)
        menubar.add_cascade(label="Invoice", menu=invoice_menu)

        # Display the menu
        self.root.config(menu=menubar)

        pass
            
    # Functions to create child frames 
    # when menu options are selected

    def create_staff_gui(self):
        # Destroy whatever the current GUI is
        # and create Staff GUI
        if self.current_gui:
            self.current_gui.destroy()

        staff_gui = StaffGUI()
        self.current_gui = staff_gui.create_gui(self.root)
        pass

    def create_customer_gui(self):
        # Destroy whatever the current GUI is
        # and create Staff GUI
        if self.current_gui:
            self.current_gui.destroy()

        customer_gui = CustomerGUI()
        self.current_gui = customer_gui.create_gui(self.root)
        pass

if __name__ == '__main__':
    gui = RCBSGUI()
    gui.root.mainloop()
    pass        