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
