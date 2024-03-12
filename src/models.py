import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    favorites = relationship("Favorite", back_populates="user")

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    gender = Column(String)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))

    homeworld = relationship("Planet", back_populates="residents")

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    terrain = Column(String)

    residents = relationship("Character", back_populates="homeworld")

class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))

    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")
