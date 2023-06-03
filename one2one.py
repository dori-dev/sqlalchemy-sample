from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///country.db')
base = declarative_base()
session = sessionmaker(bind=engine)()


class Country(base):
    __tablename__ = 'country'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    capital = relationship('Capital', backref='country', uselist=False)


class Capital(base):
    __tablename__ = 'capital'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    country_id = Column('country_id', Integer, ForeignKey('country.id'))


base.metadata.create_all(engine)


iran = Country(name='Iran')
session.add(iran)
session.commit()

tehran = Capital(name='Tehran', country=iran)
session.add(iran)
session.commit()

print(session.query(Country).first().capital.name)
