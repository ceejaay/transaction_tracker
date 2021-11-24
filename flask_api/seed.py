from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
DATABASE_URI = 'postgresql+psycopg2://cjem:password@localhost/friends_repo'
Base = declarative_base()

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)


user = User(name="Chad")
session.add(user)
session.commit()
# Base.metadata.create_all(engine)


# User.__table__
# Table('users', MetaData(),
#         Column('id', Integer(), table='friends_repo', primary_key=True, nullable=False),
#         Column('name', String(), table='friends_repo')
#         )

