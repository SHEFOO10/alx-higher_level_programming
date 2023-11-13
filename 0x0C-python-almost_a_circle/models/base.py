#!/usr/bin/python3
""" Base Class """
import json
import os


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiate new object"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file
        """
        with open(f'{cls.__name__}.json', 'w', encoding='UTF-8') as f:
            if list_objs is None:
                json.dump([], f)
                return
            f.write(Base.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)
