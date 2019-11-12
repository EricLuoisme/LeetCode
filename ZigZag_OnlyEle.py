
def convert(s: str, numRows: int) -> str:

    line_string = '' # store this line's output

    if numRows == 1:
        # if numRows is one, just return the string
        return s

    if numRows == 2:
        # if numRows is one, just return the string
        first_s = ''
        second_s = ''
        for i in range(0, len(s)):
            if i%2 == 0:
                first_s += s[i]
            else:
                second_s += s[i]
        return first_s + second_s

    # if numRows > 2
    for i in range(0, numRows):
        c = 0 # index which number of this row
        if i == 0: # for the first row
            row_ele_index = getRowEleIndex(c + 1, numRows)
            while row_ele_index < len(s):
                line_string += s[row_ele_index]
                c += 1
                row_ele_index = getRowEleIndex(c + 1, numRows)

        elif i == numRows - 1: # the last row
            row_ele_index = getRowEleIndex(c + 1, numRows) + i
            while row_ele_index < len(s):
                line_string += s[row_ele_index]
                c += 1
                row_ele_index = getRowEleIndex(c + 1, numRows) + i

        else: # for other rows
            row_ele_index = getRowEleIndex(c + 1, numRows) + i
            if row_ele_index >= len(s):
                break
            else:
                line_string += s[row_ele_index]
                c += 1 # go to second element in this row
                while row_ele_index < len(s):
                    row_ele_index = getRowEleIndex(c + 1, numRows) - i # ele between two vertical line
                    if row_ele_index >= len(s):
                        break
                    else:
                        line_string += s[row_ele_index]

                    row_ele_index = getRowEleIndex(c + 1, numRows) + i # element in the vertical line
                    if row_ele_index >= len(s):
                        break
                    else:
                        line_string += s[row_ele_index]
                    c += 1

    return line_string


def getRowEleIndex(r_n, numRows):
    row_ele_index = (r_n - 1) * (4 + (numRows - 3) * 2)
    return row_ele_index




# print(convert("A", 1))
# print(convert("ABDCSADA", 2))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 6))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 7))

print([''] * 5)
