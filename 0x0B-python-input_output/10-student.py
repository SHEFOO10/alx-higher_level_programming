#!/usr/bin/python3
""" 9. Student to JSON """


class Student:
    """ defines a student """
    def __init__(self, first_name, last_name, age):
        """
            initialization of the object

            Args:
                first_name (str): first name.
                last_name (str): last name.
                age (int): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            filtered_dict = {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
            return filtered_dict
        else:
            return self.__dict__
