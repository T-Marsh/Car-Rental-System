from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # Note to Self:
    #   echo=False means do not show generated SQL statements
    #   echo=True means do show generated SQL statements
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 