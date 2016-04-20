import re

def binary(text):
    return re.match(r'^[0-1]+$', text)

def binary_even(text):
    return re.match(r'^[0-1]+0$', text)

def hex(text):
    return re.findall(r'^[A-F0-9]+$', text)

def word(text):
    return re.findall(r'^[0-9]{,2}-?[A-Za-z-?]+$', text)

def words(text):
    words = re.findall(r'^[0-9]{,2}-?[A-Za-z-?]+$', text)
    count = len(words)
    if count:
        if len(words) != count:
            return False
