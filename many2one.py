from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///school.db')
base = declarative_base()
session = sessionmaker(bind=engine)()


class Student(base):
    __tablename__ = 'student'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    classroom_id = Column('classroom_id', Integer, ForeignKey('classroom.id'))


class ClassRoom(base):
    __tablename__ = 'classroom'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    students = relationship('Student', backref='classroom')


base.metadata.create_all(engine)


c1 = ClassRoom(name='class a')
session.add(c1)
session.commit()

s1 = Student(name='ali', classroom=c1)
s2 = Student(name='mmd', classroom=c1)
session.add_all([s1, s2])
session.commit()

for student in c1.students:
    print(student.name)
