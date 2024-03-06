#!/usr/bin/env python3
""" This module serializes and desrializes BaseModel instances
and makes it persistent using the class FileStorage.
"""
import json
import os


class FileStorage:
    """ This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects.
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """ This method sets the obj in __objects dictionary
        with key `<obj class name>.id`
        Args:
            obj: object being added to the __objects dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ This method serializes the __objects dictionary
        to the JSON file.
        """
        with open(FileStorage.__file_path, "w") as f:
            newdict = {}
            for key, value in FileStorage.__objects.items():
                newdict[key] = value.to_dict()
            f.write(json.dumps(newdict))

    def reload(self):
        """ This methos deserializes the JSON file to the
        __objects dictionary only if the JSON file exists.
        otherwise, it'll do nothing.
        """
        from models.base_model import BaseModel
        if (os.path.exists(FileStorage.__file_path) and
                os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                loaded = json.loads(f.read())
                for key, value in loaded.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        else:
            pass