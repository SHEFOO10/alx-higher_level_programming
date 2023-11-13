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
        if list_objs is None:
            return []
        new_list = []
        for obj in list_objs:
            new_list.append(obj.to_dictionary())
        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(Base.to_json_string(new_list))
