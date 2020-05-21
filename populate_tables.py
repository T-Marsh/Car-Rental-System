from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dateutil.parser import parse

from schema import Staff
from schema import Booking
from schema import Customer
from schema import Car
from schema import Invoice

DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # echo=False means do not show generated SQL statements
    # Can be set to echo=True to show SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

def populate():

    # Get a session
    session = get_db_session()

    # Staff data
    session.add_all([
        Staff(staff_name = 'Thomas', 
            staff_surname = 'Marsh', 
            staff_password = 'password'),

        Staff(staff_name = 'Jane', 
            staff_surname = 'Doe', 
            staff_password = '123abc'),

        Staff(staff_name = 'John', 
            staff_surname = 'Smith', 
            staff_password = 'qwerty')  
        ])

    # Customer data
    session.add_all([
        Customer(customer_name='Clifford', 
            customer_surname='Lloyd', 
            customer_address='1 Chapel Street', 
            customer_city='Melbourne', 
            customer_state='Victoria', 
            customer_postcode=3001, 
            customer_phone="0312345678"),

        Customer(customer_name='Sam', 
            customer_surname='Brown', 
            customer_address='12 Main Street', 
            customer_city='Geelong', 
            customer_state='Victoria', 
            customer_postcode=3001, 
            customer_phone="0375385784"),

        Customer(customer_name='Clifford', 
            customer_surname='Lloyd', 
            customer_address='1 Chapel Street', 
            customer_city='Warrnambool', 
            customer_state='South Australia', 
            customer_postcode=3001, 
            customer_phone="0369303950")
    ])

    # Car data
    session.add_all([
        Car(car_make='Jeep', 
            car_model='Cherokee', 
            car_colour='Blue'),

        Car(car_make='Ford', 
            car_model='GT', 
            car_colour='Yellow'),

        Car(car_make='Toyota', 
            car_model='Corola', 
            car_colour='Gray')   
    ])

    # Booking data
    session.add_all([
        Booking(customer_id=1, 
            car_registration=2, 
            staff_id=3,
            booking_date_start='21/02/20',
            booking_date_end='30/07/20',
            booking_comments='None.'),

        Booking(customer_id=3, 
            car_registration=1, 
            staff_id=2,
            booking_date_start='04/12/20',
            booking_date_end='30/12/20',
            booking_comments='Something.'),

        Booking(customer_id=2, 
            car_registration=3, 
            staff_id=2,
            booking_date_start='21/04/20',
            booking_date_end='10/09/20',
            booking_comments='N/A')  
    ])

    # Invoice data
    session.add_all([
        Invoice(booking_id=3, 
            invoice_date='21/04/20', 
            invoice_cost=1000.50),

        Invoice(booking_id=2, 
            invoice_date='04/12/20', 
            invoice_cost=800.37),

        Invoice(booking_id=1, 
            invoice_date='07/09/20', 
            invoice_cost=10020.51)
    ])

    # Commit the transactions
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
        populate()
