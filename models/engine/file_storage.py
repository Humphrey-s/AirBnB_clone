#!/usr/bin/python3
import json
import os

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def __init__(self):

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):

        with open(self.__file_path, "w+", encoding="utf-8") as f:
            json.dump(self.__objects, f, default=lambda o: str(o))

    def reload(self):

        if os.path.exists(self.__file_path):

            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = json.load(f)
