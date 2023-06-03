from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import and_

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
session = sessionmaker(bind=engine, autocommit=True)()


class Student(base):
    __tablename__ = 'student'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))


base.metadata.create_all(engine)

# select
students = session.query(Student).order_by(Student.id).all()
for student in students:
    print(student.id, student.name)

students = session.query(Student).filter(Student.name == 'ali')
print(students.count())
students = session.query(Student).filter(
    and_(Student.name == 'ali', Student.id == 2)
)

# insert
s1 = Student(name='ali')
# session.add(s1)
# session.commit()

s2 = Student(name='saman')
# session.add_all([s1, s2])
# session.commit()


# delete

student = session.query(Student).filter(Student.name == 'saman').delete()


# update
session.query(Student).filter(Student.name == 'mohammad').update(
    {'name': 'mmd'},
)
