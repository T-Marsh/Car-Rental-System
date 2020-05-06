from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float, Date, ForeignKey

Base = declarative_base()

class Staff(Base):
    
    __tablename__ = 'staff'

    staff_id = Column(Integer, primary_key=True)
    staff_name = Column(String(255), nullable=False)
    staff_surname = Column(String(255), nullable=False)
    staff_password = Column(String(255), nullable=False)

class Customer(Base):
    
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(255), nullable=False)
    customer_surname = Column(String(255), nullable=False)
    customer_address = Column(String(255), nullable=False)
    customer_city = Column(String(255), nullable=False)
    customer_state = Column(String(255), nullable=False)
    customer_postcode = Column(Integer, nullable=False)
    customer_phone = Column(String(10), nullable=False, unique=True)

class Car(Base):

    __tablename__ = 'car'

    car_registration = Column(Integer, primary_key=True)
    car_make = Column(String(255), nullable=False)
    car_model = Column(String(255), nullable=False)
    car_colour = Column(String(255), nullable=False)

class Booking(Base):
    
    __tablename__ = 'booking'

    booking_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    car_registration = Column(Integer, ForeignKey("car.car_registration"))
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    booking_date_start = Column(Date, nullable=False)
    booking_date_end = Column(Date, nullable=False)
    booking_comments = Column(String(255), nullable=True)

class Invoice(Base):
    
    __tablename__ = 'invoice'

    invoice_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey("booking.booking_id"))
    invoice_date = Column(Date, nullable=False)
    invoice_cost = Column(Float, nullable=False)