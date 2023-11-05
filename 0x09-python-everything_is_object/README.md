## 0x09-python-everything_is_object




**100-magic_string.py**
```
    
    magic_string.counter = getattr(magic_string, "counter", 0) + 1
```
getattr is a built-in Python function used to retrieve the value of an attribute (such as a method or variable) of an object. It is commonly used to access object attributes, including instance attributes and class attributes. The function takes three arguments:

The object you want to access an attribute from.
A string specifying the name of the attribute you want to access.
An optional default value to return if the attribute does not exist.
Here's the syntax of getattr:

getattr(object, attribute, default)
object: This is the object you want to retrieve an attribute from. It can be any Python object, such as a module, class, instance, or even a built-in type like a list or dictionary.

`attribute`: This is a string representing the name of the attribute you want to access.

`default`: This is an optional argument. If provided, getattr will return this value if the specified attribute does not exist. If default is not provided and the attribute does not exist, getattr will raise an AttributeError.

------------------


**101-locked_class.py**

In Python, the `__slots__` attribute is a special attribute that can be defined in a class to explicitly declare a fixed set of instance attributes. It's a way to optimize memory usage and improve attribute access times for instances of the class. By specifying `__slots__`, you restrict the set of attributes that can be assigned to instances of that class, and Python will store those attributes more efficiently.