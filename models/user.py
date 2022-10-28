#!/usr/bin/python3
"""Define class User which inherits from BaseModel"""

from models.base_model import BaseModel

class User(BaseModel):
    """
        create a new User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

