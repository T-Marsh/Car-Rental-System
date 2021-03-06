from sqlalchemy import create_engine
from schema import Base 

DATABASE_URI = 'sqlite:///app.db'

engine = create_engine(DATABASE_URI, echo=False)
# Note to Self:
    #   echo=False means do not show generated SQL statements
    #   echo=True means do show generated SQL statements

# Create database and tables
Base.metadata.create_all(engine)

print("Car Rental System database created.")