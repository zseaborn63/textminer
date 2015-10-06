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
    good_symbol = re.findall(r"(\$)", some_money)
    good_money = re.findall(r"(\d*\.?\d+?)", some_money)
    if good_symbol:
        if len(good_symbol) != 1:
            return None
    if good_money == []:
        return None
    if "." in good_money:
        if len(good_money[-1]) != 1:
            return None
        if len(good_money[-2]) < 5:
            return None
        else:
            good_num = "".join(good_money)
        good_num = float(good_num)
        return {'currency': good_symbol[0], 'amount': good_num}
    else:
        good_num = "".join(good_money)
        good_num = float(good_num)
        return {'currency': good_symbol[0], 'amount': good_num}


def zipcode(some_zipcode):
    x = re.search(r"(\d{5})-?(\d{0,4})?", some_zip)
    if x:
        if len(x.group(2)) == 0:
            return {"zip": "{}".format(x.group(1)), "plus 4": "{}".format(None)}
        elif len(x.group(2)) == 4:
            return {"zip": "{}".format(x.group(1)), "plus 4": "{}".format(x.group(2))}
        else:
            return None
    else:
        return None


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
        return ddict
    else:
        return None
