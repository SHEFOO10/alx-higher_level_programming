#!/usr/bin/python3
""" 13. Search and update """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    after each line containing a specific string
    """
    with open(filename, 'r', encoding='UTF8') as file:
        content = file.read().split('\n')
        new_content = []
        for line in content:
            if search_string in line:
                new_content.append(line + '\n' + new_string.replace('\n', ''))
            else:
                new_content.append(line)
    with open(filename, 'w', encoding='UTF8') as file:
        file.write('\n'.join(new_content))
