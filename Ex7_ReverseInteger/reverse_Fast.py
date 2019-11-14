
def reverse(x: int) -> int:
    # just using slice to reverse an string

    # if we put s = str(x), then manipulate over s, it would be really slow
    # but directly using str(x)[::-1], it would be faster

    if x >= 0:
        rev = int(str(x)[::-1])
        if rev > 2**31 -1:
            return 0
    else:
        rev = - int(str(x)[1:][::-1])
        if rev < - 2**31:
            return 0
    return rev



print(reverse(1534236469))
