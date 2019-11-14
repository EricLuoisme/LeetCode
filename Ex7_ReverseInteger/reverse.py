
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21


def reverse(x: int) -> int:

    rev = 0
    if x < 0:
        m = -1
    else:
        m = 1
    x = x * m

    while x / 10 > 0:
        rev *= 10
        rev += x % 10
        x = x // 10

    if rev < - 2**31 or rev > 2**31 - 1:
        return 0
    else:
        return rev * m



print(reverse(1534236469))
