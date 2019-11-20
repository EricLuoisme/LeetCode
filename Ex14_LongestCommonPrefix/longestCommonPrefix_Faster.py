
def longestCommonPrefix(strs) -> str:

    pref = ''
    let = zip(*strs)
    for chr in let:
        if len(set(chr)) > 1:
            return pref
        else:
            pref += chr[0]
    return pref


s = ["flower","flow","flight"]
s = ["", "t"]
s = ["c", "c"]
print(longestCommonPrefix(s))
