#!/usr/bin/python3
""" 13. Search and update """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    after each line containing a specific string
    """
    with open(filename, 'r+', encoding='UTF8') as file:
        content = file.readlines()
        i = 0
        for line in content:
            if line.find(search_string) != -1:
                content.insert(i + 1, new_string)
            i += 1
        file.seek(0)
        file.write("".join(content))
