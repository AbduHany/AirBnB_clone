#!/usr/bin/env python3
""" This module defines the class ``BaseModel``
"""
import uuid
import datetime


class BaseModel:
    """ This class defines all common attributes/methods
    for other classes in the AirBnB_clone project
    """
    def __init__(self):
        """ This method initializes a BaseModel object/instance.
        Assigns id attribute with uuid4(), created_at with the
        datetime object when the instance is created, and
        updated_at with the datetime object when the instance is updated.
        """
        self.id = str(uuid.uuid4().hex)
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ This method prints the string representation of a BaseModel
        object/instance.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ This method updates the updated_at attribute with the current
        datetime object.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ This method returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        instance_dict = dict(self.__dict__)
        instance_dict['__clas__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return (instance_dict)