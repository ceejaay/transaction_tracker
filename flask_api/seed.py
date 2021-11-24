import uuid
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import UUID
from faker import Faker

fake = Faker()
DATABASE_URI = 'postgresql+psycopg2://cjem:password@localhost/homework_dev'
Base = declarative_base()

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    inserted_at=Column(DateTime, nullable=False)
    updated_at=Column(DateTime, nullable=False)


user = User(id=uuid.uuid1(), first_name="Chad", last_name="Jem", dob="02251875", inserted_at=datetime.now(),
        updated_at=datetime.now)

session.add(user)
session.commit()

# for i in range(1, 10):
#     print(i)
#     user = User(name=fake.name())
#     session.add(user)
#     session.commit()
    # Base.metadata.create_all(engine)


# User.__table__
# Table('users', MetaData(),
#         Column('id', Integer(), table='friends_repo', primary_key=True, nullable=False),
#         Column('name', String(), table='friends_repo')
#         )

