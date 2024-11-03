#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine import storage_type

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False) if storage_type == 'db' else ''
    
    # Define a relationship with City
    cities = relationship('City', back_populates='state', cascade="all, delete-orphan")

    @property
    def get_cities(self):
        """Getter for cities when storage type is not db"""
        from models.__init__ import storage
        from models.city import City
        return [city for city in storage.all(City).values() if city.state_id == self.id]
