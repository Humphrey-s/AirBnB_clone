#!/usr/bin/python3
"""Class BaseModel"""
import uuid
import datetime

class BaseModel:

    def __init__(self, name=None, my_number=None):

        self.name = name
        self.my_number = my_number
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):

        BMstring = "[" + str(type(self).__name__) + "] "
        BMstring += " (" + str(self.id) + ") "
        BMstring += str(self.__dict__)

        return BMstring

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        
        b = self.__dict__

        b["__class__"] = type(self).__name__
        b["updated_at"] = self.updated_at.isoformat()
        b["created_at"] = self.created_at.isoformat()

        return b
