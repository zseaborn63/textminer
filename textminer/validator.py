import re


def binary(some_nums):
    z = re.search(r"\D", nums)
    if z:
        return False
    else:
        x = re.findall(r"[2-9]", nums)
        if x:
            return False
        else:
            return True


def binary_even(some_nums):
    x = re.findall(r"[2-9]", nums)
    if x:
        return False
    else:
        y = re.search(r"0$", nums)
        if y:
            return True
        else:
            return False


def hexidecimal(some_nums):
     x = re.search(r"[G-Z]", num)
    if x:
        return False
    else:
        return True


def word(some_string):
    x = re.findall(r"(\w\S+[^0-9][^!_*])", some_string)
    if x:
        y = re.search(r"[!*_]", some_string)
        if y:
            return False
        else:
            return True
    else:
        return False


def words(some_string, yes_or_no):
    x = re.findall(r"(\w\S+[^0-9][^!_*])", some_string)
    if x:
        y = re.search(r"[!*_]", some_string)
        if yes_or_no == "yes":
            count = len(x)
            if y:
                return False, count
            else:
                return True, count
        else:
            count = None
            if y:
                return False
            else:
                return True, count
    else:
        return False


def phone_number(some_num):
    good_num = re.search(r"\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})", some_num)
    if good_num:
        return True
    else:
        return False


def money(some_money):
    good_symbol = re.findall(r"(\$)", some_money)
    good_money = re.findall(r"(\d*\.?\d+?)", some_money)
    if good_symbol:
        if len(good_symbol) != 1:
            return False
    if good_money == []:
        return False
    if "." in good_money:
        if len(good_money[-1]) != 1:
            return False
        if len(good_money[-2]) < 5:
            return False
        else:
            return True
    elif len(good_money[0]) >= 1 and len(good_money[-1]) != 3:
        return False
    else:
        return True


def zipcode(some_zip):
    x = re.search(r"(\d{5})-?(\d{0,4})?", some_zip)
    if x:
        if len(x.group(2)) == 0:
            return True
        elif len(x.group(2)) == 4:
            return True
        else:
            return False
    else:
        return False


def extract_date(some_date):
    date_forms = [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
                  r"(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})",]
    for date_form in date_forms:
        match = re.match(date_form, some_date)
        if match:
            return match

def clean_date(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    return {"year": year, "month": month, "day": day}


def date(some_date):
    pot_date = extract_date(some_date)
    if pot_date:
        ddict = pot_date.groupdict()
        ddict = clean_date(**ddict)
        return True
    else:
        return False
