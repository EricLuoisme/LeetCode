
def longestCommonPrefix(strs) -> str:

    pref = ''

    if len(strs) == 0:
        return pref
    elif len(strs) == 1:
        return strs[0]

    min_str = min(strs, key=len)

    if len(min_str) == 0:
        return pref

    for i in range(len(min_str)):
        cur_char = strs[0][i]
        for st in strs:
            if cur_char != st[i]:
                return pref
        pref += cur_char
    return pref


s = ["flower","flow","flight"]
# s = ["", "t"]
# s = ["c", "c"]
print(longestCommonPrefix(s))
