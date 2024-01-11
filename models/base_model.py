#!/usr/bin/python3
"""Class BaseModel"""
import uuid
import datetime
from models import storage

class BaseModel:

    def __init__(self, *args, **kwargs):

        if len(kwargs) == 0:

            if isinstance(self, BaseModel):
                self.id = str(uuid.uuid4())
                self.created_at = datetime.datetime.now()
                self.updated_at = datetime.datetime.now()
                storage.new(self)
        else:
            for key in kwargs:
                value = kwargs[key]

                if key == "name":
                    self.name = value

                elif key == "my_number":
                    self.my_number = value
                elif key == "created_at":
                    self.created_at = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "id":
                    self.id = value
                else:
                    pass


    def __str__(self):

        BMstring = "[" + str(type(self).__name__) + "] "
        BMstring += " (" + str(self.id) + ") "
        BMstring += str(self.__dict__)

        return BMstring

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        
        b = self.__dict__

        b["__class__"] = type(self).__name__
        b["updated_at"] = self.updated_at.isoformat()
        b["created_at"] = self.created_at.isoformat()

        return b
