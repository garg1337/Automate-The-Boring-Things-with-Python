#! python3
# skornkpwdbby.py - MAKES SURE PWD IS SKRONK.

import re

eightLong = re.compile(r'''(
    (.){8,}
    )''', re.VERBOSE)

lower = re.compile(r'''(
    .*[a-z]+.*
    )''', re.VERBOSE)

upper = re.compile(r'''(
    .*[A-Z]+.*
    )''', re.VERBOSE)

digit = re.compile(r'''(
    .*\d+.*
    )''', re.VERBOSE)


while True:
    print('Gief')
    pwd = input()
    iseightLong = eightLong.match(pwd)
    hasLower = lower.match(pwd)
    hasUpper = upper.match(pwd)
    hasDigit = digit.match(pwd)
    if not iseightLong:
        print('must be at least 8 long')
    if not hasLower:
        print('must contain lowercase letters')
    if not hasUpper:
        print('must contain uppercase letters')
    if not hasDigit:
        print('needs at least one number')
    if iseightLong and hasLower and hasUpper and hasDigit:
        print('PWD IS SKRONK')
