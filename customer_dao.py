from schema import Customer

class CustomerDAO():

    def create(self, session, data):
        
        # Debugging print
        print("\nCreating a customer ...")
        print(data)

        customer = Customer (
            customer_name = data['customer_name'],
            customer_surname = data['customer_surname'],
            customer_address = data['customer_address'],
            customer_city = data['customer_city'],
            customer_state = data['customer_state'],
            customer_postcode = data['customer_postcode'],
            customer_phone = data['customer_phone']
        )

        session.add(customer)
        session.commit()

        result = {}
        result['message'] = ('Customer, {} {}, was added successfully.'.format(customer.customer_name, customer.customer_surname))
        inserted_customer_id = customer.customer_id
        result['customer_id'] = inserted_customer_id

        return result

    def find_all(self, session):
        
        # Debugging print
        print("\nFinding all customers ...")

        result = {}

        rows = session.query(Customer).all()

        if not rows:
            result['message'] = "No customers found!"
        else:
            list_customer = []
            for x in rows:
                d = {}
                d['customer_id'] = x.customer_id
                d['customer_name'] = x.customer_name
                d['customer_surname'] = x.customer_surname
                d['customer_address'] = x.customer_address
                d['customer_city'] = x.customer_city
                d['customer_state'] = x.customer_state
                d['customer_postcode'] = x.customer_postcode
                d['customer_phone'] = x.customer_phone
                list_customer.append(d)
                pass     

            result['customer'] = list_customer
           
        return result

    def find_ids(self, session):
        
        # Debugging print
        print("\nFinding all customer IDs ...")

        result = {}
 
        rows = session.query(Customer).all()

        if not rows:
            result['message'] = "No customers found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.customer_id)
                pass               

            result['customer_ids'] = list_ids
        
        return result

    def find_by_id(self, session, customer_id):
        
        # Debugging print
        print("\nFinding a customer of ID: {} ...".format(customer_id))

        cust = session.query(Customer).get(customer_id) 
        
        result = {}

        if not cust:
            result['message'] = ("Customer with an ID of {} was NOT found!".format(customer_id))
        else:
            d = {}
            d['customer_id'] = cust.customer_id
            d['customer_name'] = cust.customer_name
            d['customer_surname'] = cust.customer_surname
            d['customer_address'] = cust.customer_address
            d['customer_city'] = cust.customer_city
            d['customer_state'] = cust.customer_state
            d['customer_postcode'] = cust.customer_postcode
            d['customer_phone'] = cust.customer_phone

            result['customer'] = d           
        
        return result

    def find_by_surname(self, session, customer_surname):
        
        # Debugging print
        print("\nFinding any customer with {} as their surname ...".format(customer_surname))

        result = {}

        rows = session.query(Customer) \
               .filter(Customer.customer_surname.like(customer_surname)) \
               .order_by(Customer.customer_id).all()   

        if not rows:
            result['message'] = ("No customers with the surname {} were found!".format(customer_surname))
        else:
            list_customer = []
            for x in rows:
                d = {}
                d['customer_id'] = x.customer_id
                d['customer_name'] = x.customer_name
                d['customer_surname'] = x.customer_surname
                d['customer_address'] = x.customer_address
                d['customer_city'] = x.customer_city
                d['customer_state'] = x.customer_state
                d['customer_postcode'] = x.customer_postcode
                d['customer_phone'] = x.customer_phone
                list_customer.append(d)
                pass     

            result['customer'] = list_customer
           
        return result

    def find_by_city(self, session, customer_city):
        
        # Debugging print
        print("\nFinding any customer that lives in the city of {} ...".format(customer_city))

        result = {}

        rows = session.query(Customer) \
               .filter(Customer.customer_city.like(customer_city)) \
               .order_by(Customer.customer_id).all()   

        if not rows:
            result['message'] = ("No customers were found to live in {}!".format(customer_city))
        else:
            list_customer = []
            for x in rows:
                d = {}
                d['customer_id'] = x.customer_id
                d['customer_name'] = x.customer_name
                d['customer_surname'] = x.customer_surname
                d['customer_address'] = x.customer_address
                d['customer_city'] = x.customer_city
                d['customer_state'] = x.customer_state
                d['customer_postcode'] = x.customer_postcode
                d['customer_phone'] = x.customer_phone
                list_customer.append(d)
                pass     

            result['customer'] = list_customer
           
        return result

    def find_by_state(self, session, customer_state):
        
        # Debugging print
        print("\nFinding any customer that lives in the state of {} ...".format(customer_state))

        result = {}

        rows = session.query(Customer) \
               .filter(Customer.customer_state.like(customer_state)) \
               .order_by(Customer.customer_id).all()   

        if not rows:
            result['message'] = ("No customers were found to live in {}!".format(customer_state))
        else:
            list_customer = []
            for x in rows:
                d = {}
                d['customer_id'] = x.customer_id
                d['customer_name'] = x.customer_name
                d['customer_surname'] = x.customer_surname
                d['customer_address'] = x.customer_address
                d['customer_city'] = x.customer_city
                d['customer_state'] = x.customer_state
                d['customer_postcode'] = x.customer_postcode
                d['customer_phone'] = x.customer_phone
                list_customer.append(d)
                pass     

            result['customer'] = list_customer
           
        return result

    def find_by_postcode(self, session, customer_postcode):

        # Debugging print
        print("\nFinding any customer that lives in the postcode of {} ...".format(customer_postcode))

        result = {}

        rows = session.query(Customer) \
               .filter(Customer.customer_postcode.like(customer_postcode)) \
               .order_by(Customer.customer_id).all()   

        if not rows:
            result['message'] = ("No customers were found to live in postcode of {}!".format(customer_postcode))
        else:
            list_customer = []
            for x in rows:
                d = {}
                d['customer_id'] = x.customer_id
                d['customer_name'] = x.customer_name
                d['customer_surname'] = x.customer_surname
                d['customer_address'] = x.customer_address
                d['customer_city'] = x.customer_city
                d['customer_state'] = x.customer_state
                d['customer_postcode'] = x.customer_postcode
                d['customer_phone'] = x.customer_phone
                list_customer.append(d)
                pass     

            result['customer'] = list_customer
           
        return result    

    def update(self, session, customer_id, data):
        
        # Debugging print
        print("\nUpdating customer with an ID of: {} ...".format(customer_id))

        result = {}

        cust = session.query(Customer).get(customer_id)

        if not cust:
            result['message'] = ("No customer with ID of {} to update!".format(customer_id))
        else:
            print("Customer details before update:")
            print("\tName > ", cust.customer_name)
            print("\tSurname > ", cust.customer_surname)
            print("\tAddress > ", cust.customer_address)
            print("\tCity > ", cust.customer_city)
            print("\tState > ", cust.customer_state)
            print("\tPostcode > ", cust.customer_postcode)
            print("\tPhone > ", cust.customer_phone)

            
            cust.customer_name = data['customer_name']
            cust.customer_surname = data['customer_surname']
            cust.customer_address = data['customer_address']
            cust.customer_city = data['customer_city']
            cust.customer_state = data['customer_state']
            cust.customer_postcode = data['customer_postcode']
            cust.customer_phone = data['customer_phone']

            print("Customer details after update:")
            print("\tName > ", cust.customer_name)
            print("\tSurname > ", cust.customer_surname)
            print("\tAddress > ", cust.customer_address)
            print("\tCity > ", cust.customer_city)
            print("\tState > ", cust.customer_state)
            print("\tPostcode > ", cust.customer_postcode)
            print("\tPhone > ", cust.customer_phone)

            session.commit()
            result['message'] = "Customer updated."  

        return result

    def delete(self, session, customer_id):
        
        # Debugging print
        print("\nDeleting customer with an ID of: {} ...".format(customer_id))
 
        result = {}
    
        cust = session.query(Customer).get(customer_id)

        if not cust:
            result['message'] = ("No customers with an ID of {} were found!".format(customer_id))
        else:
            session.delete(cust)
            session.commit()
            result['message'] = "Customer deleted."    

        return result