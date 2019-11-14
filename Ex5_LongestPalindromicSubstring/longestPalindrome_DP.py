
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


def longestPalindrome(s):

    # by using dynamic programming
    if len(s) == 0:
        return None

    total_len = len(s)
    start_index = 0
    max_length = 1

    # set up an table to store whether a substring is a palindrome
    table = []
    for i in range(0, total_len):
        row = []
        for j in range(0, total_len):
            row.append(False)
        table.append(row)

    # all single character is also a palindrome
    for i in range(0, total_len):
        table[i][i] = True

    # finding two connect same character substring is also a palindrome (e.g. "aa")
    for i in range(0, total_len - 1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            start_index = i
            max_length = 2

    palin_in_len = 3 # it represent current length of palindrome that we are looking
                    # because all single character is palindrome, with length 1
                    # all "aa" like string also palindrome, with length 2
                    # here we start finding a palindrome with length 3

    # for i in range(total_len - palin_in_len + 1):
    #     print(i)

    while palin_in_len <= total_len:
        for i in range(total_len - palin_in_len + 1):
            j = i + palin_in_len - 1
            # j is the exactly 'end' character we need to check, i is the 'start'
            if s[i] == s[j] and table[i+1][j-1] == True:
                # table[i+1][j-1] means to check the string between i and
                # j is a palidrome or not
                table[i][j] = True # record that the string from i to j is a palidrome
                if max_length < palin_in_len:
                    start_index = i # means new palidrome start from this index
                    max_length = palin_in_len # record the max length

        palin_in_len += 2 # find a bigger palindrome

    return s[start_index : start_index + max_length]
    # we know where the palidrome start, can get it with it's length



print(longestPalindrome("abacab"))
