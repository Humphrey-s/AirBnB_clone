#!/usr/bin/python3
"""Class BaseModel"""
from uuid import uuid4
from datetime import datetime
from models import storage

Tformat = "%Y-%m-%d %H:%M:%S"

class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs is None:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow().strftime(Tformat)
            self.updated_at = datetime.utcnow().strftime(Tformat)
        else:

            for key, value in kwargs.items():
                setattr(self, key, value)
            if "id" not in kwargs.keys():
                self.id = str(uuid4())
                self.created_at = datetime.utcnow().strftime(Tformat)
                self.updated_at = datetime.utcnow().strftime(Tformat)
            else:
                if "created_at" not in kwargs.keys():
                    self.created_at = datetime.now().strftime(Tformat)
                else:
                    self.updated_at = datetime.now().strftime(Tformat)

    def __str__(self):
        """return string rep of an instance"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
    def save(self):
        """save instance"""
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns dict representation of instance"""
        new_dct = self.__dict__
        new_dct["updated_at"] = datetime.now().strftime(Tformat)
        new_dct["created_at"] = datetime.now().strftime(Tformat)
        new_dct["__class__"] = self.__class__.__name__

        return new_dct
