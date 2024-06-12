
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    items = relationship("Item", backref="category")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))

    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', category_id={self.category_id})"
