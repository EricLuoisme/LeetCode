
def myAtoi(s: str) -> int:

    ls = list(s.strip())

    if len(ls) == 0:
        return 0

    if ls[0] == '-':
        sign = -1
    else:
        sign = 1

    if ls[0] in ['-', '+']:
        del ls[0]

    result = 0
    i = 0
    while i < len(ls) and ls[i].isdigit():
        result = result * 10 + int(ls[i])
        i += 1

    return max(min(result * sign, 2**31 - 1), - 2**31)


# print(myAtoi('-234'))
