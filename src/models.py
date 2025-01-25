import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(250), primary_key=True, unique=True)
    email = Column(String(60), nullable=False,unique=True)
    password = Column(String(35), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=True)
    birth_year = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    height = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)
    favorites = relationship("Favorite", back_populates="character")
    def to_dict(self):
        return {   
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass
            }

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    rotation = Column(Integer, nullable=True)
    orbit = Column(Integer, nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(Integer, nullable=True)
    favorites = relationship("Favorite", back_populates="planet")
    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "diameter": self.diameter,
            "population": self.population,
            "rotation": self.rotation,
            "orbit": self.orbit,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self
        }
class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = Column(String(250), ForeignKey('user.name'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'),nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'),nullable=True)
    planet = relationship("Planet", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
