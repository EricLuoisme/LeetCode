
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

    # i = 2 # slower
    # n = 1
    # mod_num = 3
    # the_set = []
    #
    # # build the dictionary
    # for a in ascii_lowercase:
    #     the_set.append(a)
    #     if i == 7 or i == 9:
    #         mod_num = 4
    #     else:
    #         mod_num = 3
    #     if n % mod_num == 0:
    #         dic[i] = the_set
    #         i += 1
    #         the_set = []
    #         n = 0
    #     n += 1

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
