"""
Test is best done on an empty database as staff_id of 1 is used
And it can be run more than once
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from staff_dao import StaffDAO

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
Test the create() method of the StaffDAO class
'''
def test_create():

    session = get_db_session()
    
    stf = StaffDAO()

    data = {
        'staff_name':"Thomas",
        'staff_surname': "Marsh",
        'staff_password': "qwerty"
    }

    result = stf.create(session, data)

    print(result)

    session.close()

def test_find_by_id():
    
    session = get_db_session()
    
    stf = StaffDAO()

    staff_id = 1    # Test Case 1
    # staff_id = 2  # Test Case 2

    result = stf.find_by_id(session, staff_id)

    print(result)
    
    session.close()

def test_find_all():
    
    session = get_db_session()
    
    stf = StaffDAO()

    result = stf.find_all(session)

    print(result)

    session.close()    

def test_find_by_surname():
    
    session = get_db_session()
        
    stf = StaffDAO()
      
    staff_surname = "Marsh" # Test Case 1
    # staff_surname = "Lee" # Test Case 2

    result = stf.find_by_surname(session, staff_surname)

    print(result)

    session.close()  

def test_find_ids():
    
    session = get_db_session()
    
    stf = StaffDAO()

    result = stf.find_ids(session)

    print(result)

    session.close()    

def test_update():
    
    session = get_db_session()

    stf = StaffDAO()

    staff_id = 1    # Test Case 1
    # staff_id = 2   # Test Case 2

    data = {
        'staff_name':"John",
        'staff_surname': "Smith",
        'staff_password': "abc123"
    }

    result = stf.update(session, staff_id, data)

    print(result)

    session.close()    

def test_delete():
    
    session = get_db_session()
        
    stf = StaffDAO()

    staff_id = 1    # Test Case 1
    # staff_id = 2   # Test Case 2

    result = stf.delete(session, staff_id)

    print(result)

    session.close()          

if __name__ == "__main__":

    print("\nBeginning test of staff_dao.py ...")

    test_create()
    
    test_find_by_id()

    test_find_all()

    test_find_by_surname()

    test_find_ids()

    test_update()

    test_delete()

    print("\nEnd of test ...")