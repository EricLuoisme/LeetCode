
from string import ascii_lowercase
from itertools import product


def letterCombinations(digits: str):

    if digits == '':
        return ''

    dic = {}
    dic[2] = {'a', 'b', 'c'} # faster
    dic[3] = {'d', 'e', 'f'}
    dic[4] = {'g', 'h', 'i'}
    dic[5] = {'j', 'k', 'l'}
    dic[6] = {'m', 'n', 'o'}
    dic[7] = {'p', 'q', 'r', 's'}
    dic[8] = {'t', 'u', 'v'}
    dic[9] = {'w', 'x', 'y', 'z'}

    # get cartesian product
    temp_lists = []
    for c in digits:
        this_list = dic[int(c)]
        temp_lists.append(this_list)

    # make it in correct format
    result = []
    all_pos = list(product(* temp_lists))
    for row in all_pos:
        st = ''
        for c in row:
            st += c
        result.append(st)

    return result



print(letterCombinations(''))


# a = ['a', 'b', 'c']
# b = ['A', 'B']
# c = ['1', '2']
#
# temp = [a, b, c]
#
# print(list(product(*temp)))
