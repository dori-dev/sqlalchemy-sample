from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# database = 'postgresql'
# library = 'library'
# username = 'user1'
# password = '1234'
# host = 'localhost:port'
# db_name = ''
# engine = create_engine(
#     f'{database}+{library}://{username}:{password}@{host}/{db_name}'
# )

engine = create_engine('sqlite:///database.db')
base = declarative_base()


class Student(base):
    __tablename__ = 'student'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))


base.metadata.create_all(engine)
