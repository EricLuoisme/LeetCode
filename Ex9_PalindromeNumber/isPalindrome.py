
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


def isPalindrome(self, x: int) -> bool:

    # really fast by just using reverse of string

    rev = str(x)[::-1]
    if str(x) == rev:
        return True
    else:
        return False
