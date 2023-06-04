from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


class DB:
    _engine = create_engine('sqlite:///university.db')
    _base = declarative_base()

    def __init__(self):
        self.session_maker = sessionmaker(bind=self._engine)
        self.session = None

    def create_session(self):
        self.session = self.session_maker()

    def create_all_table(self):
        self._base.metadata.create_all(self._engine)

    class SubClass:
        id = Column(Integer, primary_key=True, autoincrement=True)

    class Person(SubClass):
        name = Column(String(50))
        family = Column(String(50))

    class Student(Person, _base):
        __tablename__ = "students"
        father = Column(String(50))
        in_classrooms = relationship(
            'ClassRoom',
            secondary='student_classroom',
            back_populates='students',
        )

    class ClassRoom(SubClass, _base):
        __tablename__ = "classrooms"
        name = Column(String(50))
        teacher_id = Column(Integer, ForeignKey('teachers.id'))
        field_id = Column(Integer, ForeignKey('fields.id'))
        students = relationship(
            'Student',
            secondary='student_classroom',
            back_populates='in_classrooms',
        )

    class Teacher(Person, _base):
        __tablename__ = "teachers"
        classrooms = relationship('ClassRoom', backref='teacher')

    class Field(SubClass, _base):
        __tablename__ = "fields"
        name = Column(String(50))
        classrooms = relationship('ClassRoom', backref='field')

    class StudentClassRoom(SubClass, _base):
        __tablename__ = "student_classroom"
        student_id = Column(Integer, ForeignKey('students.id'))
        classroom_id = Column(Integer, ForeignKey('classrooms.id'))


if __name__ == '__main__':
    db = DB()
    db.create_all_table()
    db.create_session()

    computer = db.Field(name='computer')
    art = db.Field(name='art')
    sport = db.Field(name='sport')
    db.session.add_all([computer, art, sport])
    db.session.commit()

    ali = db.Student(name='Ali', family='Mohammadi', father='Ahmad')
    salar = db.Student(name='Salar', family='Dori', father='Behrouz')
    mmd = db.Student(name='Mohammad', family='Sharif', father='Esmal')
    db.session.add_all([ali, salar, mmd])
    db.session.commit()

    teacher1 = db.Teacher(name='John', family='Smith')
    teacher2 = db.Teacher(name='Alice', family='Bob')
    db.session.add_all([teacher1, teacher2])
    db.session.commit()

    class1 = db.ClassRoom(name='A1', teacher=teacher1, field=computer)
    class2 = db.ClassRoom(name='A2', teacher=teacher1, field=computer)
    class3 = db.ClassRoom(name='B1', teacher=teacher2, field=art)
    class4 = db.ClassRoom(name='B2', teacher=teacher2, field=sport)
    db.session.add_all([class1, class2, class3, class4])
    db.session.commit()

    class1.students = [salar, mmd]
    class2.students = [ali, mmd]
    class3.students = [mmd]
    class4.students = [salar, ali]
    db.session.commit()
