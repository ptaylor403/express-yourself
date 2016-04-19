import re

def phone_numbers(text):
    number = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
    return number.search(text).groups()
