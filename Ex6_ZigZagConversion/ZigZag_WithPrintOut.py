
def convert(s: str, numRows: int) -> str:

    return_string = '' # store returning string

    for i in range(0, numRows):

        line_string = '' # store this line's output
        c = 0 # index which number of this row

        if i == 0: # for the first row
            row_ele_index = getRowEleIndex(c + 1, numRows)
            while row_ele_index < len(s):
                if c == 0: # if it's the first element in this row
                    line_string += s[row_ele_index]
                else:
                    sl, sr = getNumSpace(i, numRows)
                    line_string = line_string + sl + s[row_ele_index]
                c += 1
                row_ele_index = getRowEleIndex(c + 1, numRows)
            print(line_string)
            # return_string = getLinRealEles(return_string, line_string)

        elif i == numRows - 1: # the last row
            row_ele_index = getRowEleIndex(c + 1, numRows) + i
            while row_ele_index < len(s):
                if c == 0: # if it's the first element in this row
                    line_string += s[row_ele_index]
                else:
                    sl, sr = getNumSpace(i, numRows)
                    line_string = line_string + sr + s[row_ele_index]
                c += 1
                row_ele_index = getRowEleIndex(c + 1, numRows) + i
            print(line_string)
            # return_string = getLinRealEles(return_string, line_string)

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
                        sl, sr = getNumSpace(i, numRows)
                        line_string = line_string + sl + s[row_ele_index] + sr
                    row_ele_index = getRowEleIndex(c + 1, numRows) + i # element in the vertical line
                    if row_ele_index >= len(s):
                        break
                    else:
                        sl, sr = getNumSpace(i, numRows)
                        line_string += s[row_ele_index]
                    c += 1
            print(line_string)

        return_string = getLinRealEles(return_string, line_string)

    return return_string


def getRowEleIndex(r_n, numRows):
    row_ele_index = (r_n - 1) * (4 + (numRows - 3) * 2)
    return row_ele_index


def getNumSpace(this_row, numRows):
    # this_row start from 0
    sl = '' # for left spaces
    for i in range(0, numRows - 2 - this_row):
        sl += ' ' # empty space

    sr = '' # for right spaces
    for i in range(0, this_row - 1):
        sr += ' ' # empty space
    return sl, sr

def getLinRealEles(return_string, line_string):
    # get all real elements and return it inside the return_string
    for s in line_string:
        if s is not ' ':
            return_string = return_string + s

    return return_string





print(convert("ABCDEFG", 3))
# print(convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5))
