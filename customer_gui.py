import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox
import database as db
from customer_dao import CustomerDAO
# from validation.py import Validation

class CustomerGUI():

    def __init__(self):   
        
        # Instantiate a data access object 
        # Contains methods to access the database
        self.customer_dao = CustomerDAO()

        # Instantiate a validation object
        # Contains methods to validate input fields
        # self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.customer_id = tk.StringVar()
        self.customer_name = tk.StringVar()
        self.customer_surname = tk.StringVar()
        self.customer_address = tk.StringVar()
        self.customer_city = tk.StringVar()
        self.customer_state = tk.StringVar()
        self.customer_postcode = tk.StringVar()
        self.customer_phone = tk.StringVar()

        # List of staff ids - lb for listbox
        self.lb_ids = None

        # Messagebox title
        self.mb_title_bar = "Customer CRUD"

        pass 

    def create_gui(self, root):

        print("Creating customer GUI ...")

        sta_frame = tk.Frame(root)
        sta_frame.pack()

        form_frame = tk.Frame(sta_frame)
        form_frame.pack()
    
        tk.Label(form_frame, font=('arial', 10), 
                 text = "Customer").grid(row=0, column=0, columnspan=3)

        tk.Label(form_frame, text= "Customer Id", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.customer_id, width=30, bd=1, 
                 state=tk.DISABLED).grid(row=1, column=1)
        
        tk.Label(form_frame, text= "Customer IDs", 
                 font=('arial', 10)).grid(row=1, column=2)
        
        tk.Label(form_frame, text= "Name", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=2, column=0)
        tk.Entry(form_frame, textvariable=self.customer_name, 
                 width=30, bd=1).grid(row=2, column=1)
        
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=7) 
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        tk.Label(form_frame, text= "Surname", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=3, column=0)
        tk.Entry(form_frame, textvariable=self.customer_surname, 
                 width=30, bd=1).grid(row=3, column=1)

        tk.Label(form_frame, text= "Address", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=4, column=0)
        tk.Entry(form_frame, textvariable=self.customer_address, 
                 width=30, bd=1).grid(row=4, column=1)

        tk.Label(form_frame, text= "City", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=5, column=0)
        tk.Entry(form_frame, textvariable=self.customer_city, 
                 width=30, bd=1).grid(row=5, column=1)

        tk.Label(form_frame, text= "State", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=6, column=0)
        tk.Entry(form_frame, textvariable=self.customer_state, 
                 width=30, bd=1).grid(row=6, column=1)

        tk.Label(form_frame, text= "Postcode", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=7, column=0)
        tk.Entry(form_frame, textvariable=self.customer_postcode, 
                 width=30, bd=1).grid(row=7, column=1)

        tk.Label(form_frame, text= "Phone", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=8, column=0)
        tk.Entry(form_frame, textvariable=self.customer_phone, 
                 width=30, bd=1).grid(row=8, column=1)
        
        button_frame = tk.Frame(sta_frame, pady=10) 
        button_frame.pack()
        
        tk.Button(button_frame, width=10, text="Clear", 
                  command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Save", 
                  command=self.save).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Delete", 
                  command=self.delete).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Load", 
                  command=self.load).pack(side=tk.LEFT)       

        return sta_frame

    def clear_fields(self):
        
        self.customer_id.set("")
        self.customer_name.set("")
        self.customer_surname.set("")
        self.customer_address.set("")
        self.customer_city.set("")
        self.customer_state.set("")
        self.customer_postcode.set("")
        self.customer_phone.set("")
        pass

    def save(self):
        
        print("Saving an employee ...")

        data = self.get_fields()   

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['staff_id'])==0):
                print("Calling create() as staff_id is absent")
                self.create(data)
            else:
                print("Calling update() as staff_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass

    def get_fields(self):
        
        cust = {}
        cust['customer_id'] = self.customer_id.get() 
        cust['customer_name'] = self.customer_name.get()
        cust['customer_surname'] = self.customer_surname.get()
        cust['customer_address'] = self.customer_address.get()
        cust['customer_address'] = self.customer_city.get()
        cust['customer_state'] = self.customer_postcode.get()
        cust['customer_phone'] = self.customer_phone.get()
        return cust

    def validate_fields(self, data):
        
        # By default set to true, anything wrong will turn it to false   
        valid_data = True 
        
        message_list = [] 
        # Check for blank fields
        if len(data['staff_name'])==0:
            valid_data = False
            message_list.append("staff_name is empty")
        if len(data['staff_surname'])==0:
            valid_data = False
            message_list.append("staff_surname is empty")
        if len(data['staff_password'])==0:
            valid_data = False
            message_list.append("staff_password is empty")

        # Other possible checks

        # Implement these as functions in the Validation class so that 
        # other classes can call them
         
        # Check if firstname and lastname contain  
        # only alphabetic characters (and may be certain special characters)
        # if not self.validator.is_alphabetic(data['staff_name']):
        #     valid_data = False
        #     message_list.append("invalid staff_name")

        # if not self.validator.is_alphabetic(data['staff_surname']):
        #     valid_data = False
        #     message_list.append("invalid staff_surname")
     
        # Join the items in the list as a string separated with a comma and a space    
        message = ', '.join(message_list) 

        return valid_data, message # return 2 values

    def create(self, data):
        
        print("Creating an staff ...")
        print(data)

        session = db.get_db_session() # Get a session
        result = self.customer_dao.create(session, data)
        session.close() # Close the session

        messagebox.showinfo(self.mb_title_bar, result)

        pass

    def update(self, data):

        print("Updating a customer ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.customer_dao.update(session, data['customer_id'], data)
        session.close() # close the session
   
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def delete(self):
        
        # Grab the staff_id from the stringvar
        id = self.customer_id.get() 
        print(id)
        
        session = db.get_db_session() # Get a session (database.py)
        result = self.customer_dao.delete(session, id)
        session.close() # Close the session
  
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def load(self):
        
        session = db.get_db_session() # Get a session (database.py)
        result = self.customer_dao.find_ids(session)
        session.close() # Close the session
        print("result", result)

        # Check if there is an entry in the result dictionary
        if "customer_ids" in result: 
            list_ids = result['customer_ids']
            self.lb_ids.delete(0,tk.END)
            print("Setting customer_id in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                #print(x)
            pass
        else:
            print("There were no results!")
            messagebox.showerror("Error", "There were no results to load!")

    def on_list_select(self, evt):
        
        w = evt.widget
        index = int(w.curselection()[0]) 
          # index = position of the item clicked in the list, first item is item 0 not 1
        value = w.get(index) 
          # value of the item clicked,
        print(index) 
        print(value)

        # Call find_by_id and populate the stringvars of the form
        session = db.get_db_session() # Get a session (database.py)
        result = self.customer_dao.find_by_id(session, value)   
        session.close() # close the session
        print("result", result) 
        cust = result['customer']
        self.populate_fields(cust)
        pass

    def populate_fields(self, cust):
        
        # Set the values from the dict to the stringvars
        self.customer_id.set(cust['customer_id'])
        self.customer_name.set(cust['customer_name'])
        self.customer_surname.set(cust['customer_surname'])
        self.customer_address.set(cust['customer_address'])
        self.customer_city.set(cust['customer_city'])
        self.customer_state.set(cust['customer_state'])
        self.customer_postcode.set(cust['customer_postcode'])
        self.customer_phone.set(cust['customer_phone'])
        pass

# ###########
# Main method
# ###########

if __name__ == '__main__':
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Car Rental System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = CustomerGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass