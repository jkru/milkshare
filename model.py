from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref



engine = create_engine("sqlite:///milkshare.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, 
                                      autocommit=False,
                                      autoflush=False))
Base = declarative_base()
Base.query = session.query_property

### Class declarations

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
    drug_info = Column(Text, nullable=True)
    has_health_info = Column(Boolean, nullable=True)
    about_me = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

def get_user_by_email(email, password):
    user = session.query(User).filter_by(email=email).first()
    if user:
        if user.password != password:
            return "incorrect password"
    return user

def get_user_by_id(id):
    return session.query(User).get(id)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    #request or offer
    req_or_off = Column(String(10), nullable=False)
    date = Column(DateTime, nullable=False)
    amt_milk = Column(String(64), nullable=True)
    recurring = Column(Boolean, nullable=True)
    blurb = Column(Text, nullable=True)

    user = relationship("User", backref=backref("posts", order_by=id))

def get_posts():
    return session.query(Post).all()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    subject = Column(String(200), nullable=True)
    message = Column(Text, nullable=False)

    sender = relationship("User", foreign_keys = 'Message.sender_id', backref=backref("sent_messages", order_by=id))
    recipient = relationship("User", foreign_keys = 'Message.recipient_id', backref=backref("recieved_messages", order_by=id))

### End class declarations
def get_sent_messages(my_id):
    return session.query(Message).filter_by(sender_id=my_id)

def get_received_messages(my_id):
    return session.query(Message).filter_by(recipient_id=my_id)

def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()
