import re

def words(text):
    edited_text = re.findall(r'[0-9]{,2}[a-zA-Z-]+', text)
    if len(edited_text):
        return edited_text
    else:
        return None

def phone_numbers(text):
    area_code = re.search(r'^[0-9]{3}', text)
    number = re.search(r'[0-9]{3}-[0-9]{4}', text)
    if len(area_code) == 3:
        return area_code
    if len(number) == 8:
        return number
