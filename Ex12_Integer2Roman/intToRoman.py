
def intToRoman(num: int) -> str:

    c = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    k = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    store = {}
    for i in range(len(k)):
        store[k[i]] = c[i]

    roman = ''
    while num > 0:
        for k in store:
            if num >= k:
                roman += store[k]
                num -= k
                break

    return roman


print(intToRoman(1994))
