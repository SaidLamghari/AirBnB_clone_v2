#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.city import City
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            '''
            modification
            Returns a list of City instances with
            state_id = State.id.
            '''
            city_instances = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_instances.append(city)
            return city_instances
            

    def __init__(self, *args, **kwargs):
        """ Initializes
        modification
        a new State instance """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.cities = relationship('City', cascade='all, delete', backref='state')
