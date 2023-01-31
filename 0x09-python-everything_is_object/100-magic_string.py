#!/usr/bin/python3
def magic_string(n=[0]):
    n[0] += 1
    return str("Bestschool, " * (n[0] - 1)) + "Bestschool")
