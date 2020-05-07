"""
Test is best done on an empty database as customer_id of 1 is used
And it can be run more than once
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from customer_dao import CustomerDAO

DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # Note to Self:
    #   echo=False means do not show generated SQL statements
    #   echo=True means do show generated SQL statements
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

'''
Test the create() method of the CustomerDAO class
'''
def test_create():
    
    session = get_db_session()
    
    cust = CustomerDAO()

    data = {
        'customer_name': "Thomas",
        'customer_surname': "Marsh",
        'customer_address': "207 First Street",
        'customer_city': "Geelong",
        'customer_state': "Tasmania",
        'customer_postcode': 3205,
        'customer_phone': "0412345678"
    }

    result = cust.create(session, data)

    print(result)

    session.close()

def test_find_ids():
    
    session = get_db_session()
    
    cust = CustomerDAO()

    result = cust.find_ids(session)

    print(result)

    session.close() 

def test_find_all():
    
    session = get_db_session()
    
    cust = CustomerDAO()

    result = cust.find_all(session)

    print(result)

    session.close()

def test_find_by_id():
    
    session = get_db_session()
    
    cust = CustomerDAO()

    customer_id = 1    # Test Case 1
    # customer_id = 2  # Test Case 2

    result = cust.find_by_id(session, customer_id)

    print(result)
    
    session.close()

def test_find_by_surname():
    
    session = get_db_session()
        
    cust = CustomerDAO()
      
    customer_surname = "Marsh" # Test Case 1
    # customer_surname = "Lee" # Test Case 2

    result = cust.find_by_surname(session, customer_surname)

    print(result)

    session.close() 

def test_find_by_city():
    
    session = get_db_session()
        
    cust = CustomerDAO()
      
    customer_city = "Geelong" # Test Case 1
    # customer_city = "Melbourne" # Test Case 2

    result = cust.find_by_city(session, customer_city)

    print(result)

    session.close() 

def test_find_by_state():
    
    session = get_db_session()
        
    cust = CustomerDAO()
      
    customer_state = "Tasmania" # Test Case 1
    # customer_state = "Victoria" # Test Case 2

    result = cust.find_by_state(session, customer_state)

    print(result)

    session.close()

def test_find_by_postcode():
    
    session = get_db_session()
        
    cust = CustomerDAO()
      
    customer_postcode = 3205 # Test Case 1
    # customer_postcode = 3004 # Test Case 2

    result = cust.find_by_postcode(session, customer_postcode)

    print(result)

    session.close()

def test_update():
    
    session = get_db_session()

    cust = CustomerDAO()

    customer_id = 1    # Test Case 1
    # customer_id = 2   # Test Case 2

    data = {
        'customer_name': "John",
        'customer_surname': "Smith",
        'customer_address': "101 Main Street",
        'customer_city': "Melbourne",
        'customer_state': "Victoria",
        'customer_postcode': 3004,
        'customer_phone': "0412345678"
    }

    result = cust.update(session, customer_id, data)

    print(result)

    session.close()  

def test_delete():
    
    session = get_db_session()
        
    cust = CustomerDAO()

    customer_id = 1    # Test Case 1
    # customer_id = 2   # Test Case 2

    result = cust.delete(session, customer_id)

    print(result)

    session.close()

if __name__ == "__main__":
    
    print("\nBeginning test of customer_dao.py ...")

    test_create()

    test_find_all()

    test_find_ids()
    
    test_find_by_id()

    test_find_by_surname()

    test_find_by_city()

    test_find_by_state()

    test_find_by_postcode()

    test_update()

    test_delete()

    print("\nEnd of test ...")