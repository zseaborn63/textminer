import re


def words(some_words):
    wordy = re.findall(r"(\w\S+[^0-9])", some_words)
    if wordy == []:
        return None
    else:
        return wordy


def phone_number(some_nums):
    good_num = re.search(r"\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})", some_nums)
    if good_num:
        return {"area_code": "{}".format(*good_num.groups()), "number":, "{}-{}".format(*good_num.groups())}
    else:
        return None


def money(some_money):
    pass


def zipcode(some_zipcde):
    x = re.search(r"(\d{5})-?(\d{4})?", some_zip)
    return "{} {}".format(*x.groups())


def date(some_date):
    pass
