#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            '''
            Returns a list of City instances with
            state_id = State.id.
            '''

            c_dict = models.storage.all(City)
            return [city for city in c_dict.values()
                    if city.state_id == self.id]

    # Public getter method for cities if storage is not DBStorage
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        def cities(self):
            """
            Getter method for cities attribute.
            Returns the list of City objects linked to the current State.
            """

            c_dict = models.storage.all(models.City)
            return [city for city in c_dict.values() if city.state_id == self.id]
