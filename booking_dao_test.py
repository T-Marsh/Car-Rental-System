"""
Test is best done on an empty database as staff_id of 1 is used
And it can be run more than once
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from booking_dao import BookingDAO

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
    pass

def test_find_ids():
    pass

def test_find_all():
    pass

def test_find_by_id():
    pass

def test_find_by_customer():
    pass

def test_find_by_staff():
    pass

def test_update():
    pass

def test_delete():
    pass

if __name__ == "__main__":

    print("\nBeginning test of staff_dao.py ...")

    test_create()

    test_find_ids()

    test_find_all()
    
    test_find_by_id()

    test_find_by_customer()

    test_find_by_staff()

    test_update()

    test_delete()

    print("\nEnd of test ...")