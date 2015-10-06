import re


def phone_numbers(some_text):
    numbers = re.findall(r"(\(\d{3}\) \d{3}\-\d{4})", some_text)
    return numbers
