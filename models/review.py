#!/usr/bin/python3
""" Review module for the HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ Review classto store review information"""

    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

=======
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> 1de38e50eb65c77bcb0c043241c9e69e1dbef266
