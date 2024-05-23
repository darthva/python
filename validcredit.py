#!/usr/bin/python3
import re
def valid(cc):
    invalid= 0
    valid = 0
    pattern = r"^(?=[4-6])(?!.*(.)(-?\1){3})(\d{4}-?\d{4}-?\d{4}-?\d{4})$"
    for no in cc:
        try:
            if not re.match(pattern, no):
                print (no)
                invalid +=1
        except ValueError:
            invalid +=1
    return invalid

if __name__ == '__main__':

    arr1 = ['4253625879615786', '5122-2368-7954-3214', '5122-2368-7954 - 3214', '4424444424442444']

    res = valid(arr1)
    print (res)