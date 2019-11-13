
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring,
#     "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s: str) -> int:

    # the idea is about keep all char we had seen in cur_list,
    # once we reach a char that had already stored, we need to
    # cut the cur_list, only remain the part which just after this repeated
    # character. (if a list length is 2, we ask for [3:], it would just become
    # an empty list [])

    max_len = 0
    cur_list = []
    i = 0
    while i < len(s):
        this_char = s[i]
        if this_char not in cur_list:
            cur_list.append(this_char)
            i += 1
        else:
            cur_list = cur_list[cur_list.index(this_char) + 1:]
        if len(cur_list) > max_len:
            max_len = len(cur_list)
    return max_len


s = 'abccbaa'
print(lengthOfLongestSubstring(s))
