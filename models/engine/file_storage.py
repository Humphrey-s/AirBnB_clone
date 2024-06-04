#!/usr/bin/python3
import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def __init__(self):

        self.__file = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        """returns all objects"""
        from models.user import User
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel, "User": User}

        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """adds new object to self.__objects"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """makes and saves all changes"""
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(self.__file, "w") as f:
            json.dump(new_dict, f)

        self.reload()

    def reload(self):
        """instantiate self.__objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.review import Review
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.city import City

        classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
                "Review": Review, "State": State, "Amenity": Amenity, "City": City}

        if os.path.exists(self.__file):
            with open(self.__file, "r") as f:
                lst = json.load(f)
            for key, value in lst.items():
                d = value.copy()
                d.pop("__class__")
                self.__objects[key] = classes[value["__class__"]](**d)
