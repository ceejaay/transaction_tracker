import uuid
import random
from datetime import datetime
import pytz
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from sqlalchemy.dialects.postgresql import UUID
from faker import Faker


faker = Faker()
DATABASE_URI = 'sqlite:///flask_api_test.db'
Base = declarative_base()

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    inserted_at=Column(DateTime)
    updated_at=Column(DateTime)
    transaction = relationship("Transactions", back_populates="user", uselist=False)

class Merchant(Base):
    __tablename__ = 'merchant'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    inserted_at=Column(DateTime)
    updated_at=Column(DateTime)
    transaction = relationship("Transactions", back_populates="merchant", uselist=False)

class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer)
    credit = Column(Boolean)
    debit = Column(Boolean)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="transaction")
    merchant_id = Column(Integer, ForeignKey('merchant.id'))
    merchant = relationship("Merchant", back_populates="transaction")
    inserted_at=Column(DateTime)
    updated_at=Column(DateTime)


#################################

# creates the table
# Base.metadata.create_all(engine)

#################################

for entry in range (1, 10):
    user = User(
            first_name=faker.first_name(),
            last_name=faker.last_name(), 
            dob=faker.date_of_birth(),
            inserted_at=datetime.utcnow(), 
            updated_at=datetime.utcnow()
            )
    session.add(user)
    session.commit()

    merch = Merchant(
            name=faker.company(),
            description=faker.catch_phrase(),
            inserted_at=datetime.utcnow(),
            updated_at=datetime.utcnow()            )

    session.add(merch)
    session.commit()

    for purchase in range(1, 5):
        purchase = Transactions(
                amount=random.randrange(1, 1000),
                credit=False,
                debit=True,
                description=faker.sentence(nb_words=5),
                user_id=user.id,
                merchant_id=merch.id,
                inserted_at=datetime.utcnow(), 
                updated_at=datetime.utcnow()
                )
        session.add(purchase)
        session.commit()


#########################################
## QUERIES

## for row in session.query(User, User.first_name).all():
##     print(row.User, row.first_name)

#########################################



## for i in range(1, 10):
##     print(i)
##     user = User(name=fake.name())
##     session.add(user)
##     session.commit()
#    # Base.metadata.create_all(engine)


