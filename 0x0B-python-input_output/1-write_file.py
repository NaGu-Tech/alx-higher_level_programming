#!/usr/bin/python3
# 1-write_file.py
"""This function writes a string to a text file and returns the number of
characters written."""


def write_file(filename="", text=""):
    """This function writes astring to a text file
    Args:
    	-filename: the name of the file that is to be write to
	-text: the string to be added to the file
	"""

    with open(filename, 'w+') as f:
    return f.write(text)
