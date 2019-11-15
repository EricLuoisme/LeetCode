
def romanToInt(s: str) -> int:

    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # we must replace from the right, then no error occur
    
    s = s.replace('IV', 'IIII')
    s = s.replace('IX', 'VIIII')
    s = s.replace('XL', 'XXXX')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('CD', 'CCCC')
    s = s.replace('CM', 'DCCCC')

    sum = 0
    for c in s:
        sum += dic[c]

    return sum


print(romanToInt("IV"))
