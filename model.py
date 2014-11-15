from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text, Float, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref



engine = create_engine("sqlite:///milkshare.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, 
                                      autocommit=False,
                                      autoflush=False))
Base = declarative_base()
Base.query = session.query_property

### Class declarations go here

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=True)
    cell_phone = Column(String(15), nullable=True)
    fb_id = Column(String(64), nullable=True)
    gplus_id = Column(String(64), nullable=True)
    linkedin_id = Column(String(64), nullable=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    baby_dob = Column(DateTime, nullable=False)
    zip_code = Column(String(12), nullable=False)
    no_dairy = Column(Boolean, nullable=True)
    no_wheat = Column(Boolean, nullable=True)
    no_soy = Column(Boolean, nullable=True)
    no_caffeine = Column(Boolean, nullable=True)
    no_alcohol = Column(Boolean, nullable=True)
    drug_info = Column(Text, )
    has_health_info
    about_me
    notes

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id
    req_or_off
    date
    amt_milk
    recurring
    blurb

class Message(Base)
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    sender_id
    recipient_id
    date
    subject
    message

### End class declarations


def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()