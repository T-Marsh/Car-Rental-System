import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox
import database as db
from staff_dao import StaffDAO
# from validation.py import Validation

class StaffGUI():

    def __init__(self):   
        
        # Instantiate a data access object 
        # Contains methods to access the database
        self.staff_dao = StaffDAO()

        # Instantiate a validation object
        # Contains methods to validate input fields
        # self.validator = Validation()

        # Form fields
        # Instantiate stringvars - hold  data entered in  fields of form
        self.staff_id = tk.StringVar()
        self.staff_name = tk.StringVar()
        self.staff_surname = tk.StringVar()
        self.staff_password = tk.StringVar()

        # List of staff ids - lb for listbox
        self.lb_ids = None

        # Messagebox title
        self.mb_title_bar = "Staff CRUD"

        pass 

    def create_gui(self, root):

        print("Creating employee GUI ...")

        sta_frame = tk.Frame(root)
        sta_frame.pack()

        form_frame = tk.Frame(sta_frame)
        form_frame.pack()
    
        tk.Label(form_frame, font=('arial', 10), 
                 text = "Staff").grid(row=0, column=0, columnspan=3)

        tk.Label(form_frame, text= "Staff Id", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.staff_id, width=30, bd=1, 
                 state=tk.DISABLED).grid(row=1, column=1)
        
        tk.Label(form_frame, text= "Staff IDs", 
                 font=('arial', 10)).grid(row=1, column=2)
        
        tk.Label(form_frame, text= "Name", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=2, column=0)
        tk.Entry(form_frame, textvariable=self.staff_name, 
                 width=30, bd=1).grid(row=2, column=1)
        
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=5) 
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        tk.Label(form_frame, text= "Surname", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=3, column=0)
        tk.Entry(form_frame, textvariable=self.staff_surname, 
                 width=30, bd=1).grid(row=3, column=1)

        tk.Label(form_frame, text= "Password", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=4, column=0)
        tk.Entry(form_frame, textvariable=self.staff_password, 
                 width=30, bd=1).grid(row=3, column=1)
        
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
        
        self.staff_id.set("")
        self.staff_name.set("")
        self.staff_surname.set("")
        self.staff_password.set("")
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
        
        sta = {}
        sta['staff_id'] = self.staff_id.get() 
        sta['staff_name'] = self.staff_name.get()
        sta['staff_surname'] = self.staff_surname.get()
        sta['staff_password'] = self.staff_password.get()
        return sta

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
        result = self.staff_dao.create(session, data)
        session.close() # Close the session

        messagebox.showinfo(self.mb_title_bar, result)
 
        pass

    def update(self, data):

        print("Updating an employee ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.staff_dao.update(session, data['staff_id'], data)
        session.close() # close the session
   
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def delete(self):
        
        # Grab the staff_id from the stringvar
        id = self.staff_id.get() 
        print(id)
        
        session = db.get_db_session() # Get a session (database.py)
        result = self.staff_dao.delete(session, id)
        session.close() # Close the session
  
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def load(self):
        
        session = db.get_db_session() # Get a session (database.py)
        result = self.staff_dao.find_ids(session)
        session.close() # Close the session
        print("result", result)

        # Check if there is an entry in the result dictionary
        if "staff_ids" in result: 
            list_ids = result['staff_ids']
            self.lb_ids.delete(0,tk.END)
            print("Setting employee_id in listbox ...")
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
        result = self.staff_dao.find_by_id(session, value)   
        session.close() # close the session
        print("result", result) 
        sta = result['staff']
        self.populate_fields(sta)
        pass

    def populate_fields(self, emp):
        
        # Set the values from the dict to the stringvars
        self.staff_id.set(emp['staff_id'])
        self.staff_name.set(emp['staff_name'])
        self.staff_surname.set(emp['staff_surname'])
        self.staff_password.set(emp['staff_password'])
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
    gui = StaffGUI()

    # Create the gui
    # pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop 
    # the endless window loop to process user inputs
    root.mainloop()
    pass