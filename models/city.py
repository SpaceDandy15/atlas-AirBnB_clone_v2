#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine import storage_type

class City(BaseModel, Base):
    """This class defines a city by its attributes"""
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False) if storage_type == 'db' else ''
    name = Column(String(128), nullable=False) if storage_type == 'db' else ''
    
    # Relationship to Place
    places = relationship("Place", back_populates="cities", cascade="all, delete-orphan")
    
    # Relationship to State
    state = relationship("State", back_populates="cities")
