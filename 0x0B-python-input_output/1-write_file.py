#!/usr/bin/python3
# 1-write_file.py
""" Defines a text file line-counting function."""

def write_file(filename=""):
	"""Return the number of lines in a text file."""
	file = 0
	with open(filename) as f:
		for file in f:
			file += 1
	return file
