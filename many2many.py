from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///country.db')
base = declarative_base()
session = sessionmaker(bind=engine)()


class BookAuthor(base):
    __tablename__ = "book_author"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    book_id = Column(Integer, ForeignKey('book.id'))


class Author(base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    books = relationship(
        'Book',
        secondary='book_author',
        back_populates='authors',
    )


class Book(base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    published_at = Column(Date)
    authors = relationship(
        'Author',
        secondary='book_author',
        back_populates='books',
    )
