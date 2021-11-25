import uuid
from datetime import datetime
import pytz
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import UUID
from faker import Faker

print("uuid", uuid.uuid1())
print("timestamp", datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S'))

faker = Faker()
DATABASE_URI = 'postgresql+psycopg2://cjem:password@localhost/homework_dev'
Base = declarative_base()

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# class Pet(Base):
#     __tablename__ = 'pets'
#     id = Column(UUID(as_uuid=True), primary_key=True)
#     name = Column(String)
#     date_created = Column(DateTime, nullable=False)
#     date_updated = Column(DateTime, nullable=False)


# p = Pet(id=uuid.uuid1(), name="Rover", date_created=datetime.now(), date_updated=datetime.now())


# session.add(p)
# session.commit()

# creates the table
# Base.metadata.create_all(engine)


# the class i"m trying to work with"

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    inserted_at=Column(DateTime, nullable=False)
    updated_at=Column(DateTime, nullable=False)

# print("timestamp", datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S'))
# print(faker.date_of_birth())

user = User(
        id=uuid.uuid1(), 
        first_name=faker.first_name(),
        last_name=faker.last_name(), 
        dob=faker.date_of_birth(),
        inserted_at=datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S'), 
        updated_at=datetime.utcnow().strftime('%Y-%m-%d %H:%m:%S')
        )

# session.add(user)
# session.commit()

for row in session.query(User, User.first_name).all():
    print(row.User, row.first_name)



# for i in range(1, 10):
#     print(i)
#     user = User(name=fake.name())
#     session.add(user)
#     session.commit()
    # Base.metadata.create_all(engine)


