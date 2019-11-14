
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows # used to store that lines' elements
    l_index = 0
    step = 1

    for char in s:
        L[l_index] += char # for that line, we store a string, and add char to it
        if l_index == 0: # if the index start from above, we add char to next row
            step = 1
        if l_index == numRows - 1: # if the index reach bottom line, we
                                # need to make it write to above line
            step = -1
        l_index += step


    return ''.join(L)

print(convert("ABCDEFG", 3))
