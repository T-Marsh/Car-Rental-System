from schema import Staff

class StaffDAO():

    def create(self, session, data):

        # Debugging print
        print("\nCreating a staff member ...")
        print(data)

        staff = Staff (
            staff_name = data['staff_name'],
            staff_surname = data['staff_surname'],
            staff_password = data['staff_password']
        )

        session.add(staff)
        session.commit()

        result = {}
        result['message'] = ('Staff member {} was added successfully.'.format(staff.staff_name))
        inserted_staff_id = staff.staff_id
        result['staff_id'] = inserted_staff_id

        return result

    def find_by_id(self, session, staff_id):
        
        # Debugging print
        print("\nFinding a staff member of ID: {}".format(staff_id))

        stf = session.query(Staff).get(staff_id) 
        
        result = {}

        if not stf:
            result['message'] = ("Staff member with an ID of {} was NOT found!".format(staff_id))
        else:
            d = {}
            d['staff_id'] = stf.staff_id
            d['staff_name'] = stf.staff_name
            d['staff_surname'] = stf.staff_surname
            d['staff_password'] = stf.staff_password

            result['staff'] = d           
        
        return result

    def find_by_surname(self, session, staff_surname):
        
        # Debugging print
        print("\nFinding any staff members with {} as their surname ...".format(staff_surname))

        result = {}

        rows = session.query(Staff) \
               .filter(Staff.staff_surname.like(staff_surname)) \
               .order_by(Staff.staff_id).all()   

        if not rows:
            result['message'] = ("No staff members with the surname {} were found!".format(staff_surname))
        else:
            list_staff = []
            for x in rows:
                d = {}
                d['staff_id'] = x.staff_id
                d['staff_name'] = x.staff_name
                d['staff_surname'] = x.staff_surname
                d['staff_password'] = x.staff_password
                list_staff.append(d)
                pass     

            result['staff'] = list_staff
           
        return result

    def find_all(self, session):
        
        # Debugging print
        print("\nFinding all staff memebers ...")

        result = {}

        rows = session.query(Staff).all()

        if not rows:
            result['message'] = "No staff members found!"
        else:
            list_staff = []
            for x in rows:
                d = {}
                d['staff_id'] = x.staff_id
                d['staff_name'] = x.staff_name
                d['staff_surname'] = x.staff_surname
                d['staff_password'] = x.staff_password
                list_staff.append(d)
                pass     

            result['staff'] = list_staff
           
        return result

    def find_ids(self, session):
        
        # Debugging print
        print("\nFinding all staff member IDs ...")

        result = {}
 
        rows = session.query(Staff).all()

        if not rows:
            result['message'] = "No staff members found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.staff_id)
                pass               

            result['staff_ids'] = list_ids
        
        return result

    def update(self, session, staff_id, data):
        
        # Debugging print
        print("\nUpdating staff member with an ID of: {} ...".format(staff_id))

        result = {}

        stf = session.query(Staff).get(staff_id)

        if not stf:
            result['message'] = ("No staff member with ID of {} to update!".format(staff_id))
        else:
            print("Staff member details before update:")
            print("\tName > ", stf.staff_name)
            print("\tSurname > ", stf.staff_surname)
            print("\tPassword > ", stf.staff_password)
            
            stf.staff_name = data['staff_name']
            stf.staff_surname = data['staff_surname']
            stf.staff_password = data['staff_password']

            print("Staff member details after update:")
            print("\tName > ", stf.staff_name)
            print("\tSurname > ", stf.staff_surname)
            print("\tPassword > ", stf.staff_password)

            session.commit()
            result['message'] = "Staff member updated."  

        return result

    def delete(self, session, staff_id):
        
        # Debugging print
        print("\nDeleting staff member with an ID of: {} ...".format(staff_id))
 
        result = {}
    
        stf = session.query(Staff).get(staff_id)

        if not stf:
            result['message'] = ("No staff members with an ID of {} were found!".format(staff_id))
        else:
            session.delete(stf)
            session.commit()
            result['message'] = "Staff member deleted."    

        return result  