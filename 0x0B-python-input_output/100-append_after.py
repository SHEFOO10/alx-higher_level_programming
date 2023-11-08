#!/usr/bin/python3
""" 13. Search and update """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    after each line containing a specific string
    """
    text = ""
    with open(filename, 'r') as file:
        for line in content:
            text += line
            if line.find(search_string) != -1:
                text += new_string
    with open(filename, 'w') as file:
        file.write(text)
