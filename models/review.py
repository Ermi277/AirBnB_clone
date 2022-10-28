#!/usr/bin/python3
""" Define calss Review """

from models.base_model import BaseModel

class Review(BaseModel):
    """ Description of Review 
        Attributes:
            place_id
            user_id
            text
    """

    place_id = ""
    user_id = ""
    text = ""

