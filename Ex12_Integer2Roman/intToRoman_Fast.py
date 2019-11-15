
def intToRoman(num: int) -> str:

    # the fatest way is to thinking about: Roman note can only take care from 1 - 3999
    # then we can set all fixed stuff below

    K = ['', 'M', 'MM', 'MMM'] # 0xxx, 1xxx, 2xxx, 3xxx
    H = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    # x0xx, x1xx, x2xx, x3xx, x4xx, x5xx....
    D = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    U = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    k_c = K[num // 1000]
    h_c = H[(num % 1000) // 100]
    d_c = D[(num % 100) // 10]
    u_c = U[num % 10]

    return k_c + h_c + d_c + u_c
