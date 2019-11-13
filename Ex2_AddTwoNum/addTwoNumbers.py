
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # the below solution is following an accumulator

        head = ListNode(0) # use to store the head of the return list
        cur = head # initialise the current node we need to calculate
        carry = 0 # this is the carry if current two value would grater than 9
                    # after adding them

        while l1 is not None or l2 is not None or carry != 0:
            # here we need to specific take care of carry is not equal to 0
            val = 0 # use to store the sum of current two 'places' from two num
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            if carry != 0:
                val += 1 # an adder from last place
            carry = int(val/10) # get a carry
            cur.next = ListNode(val % 10) # get all the stuff beside the carry
            cur = cur.next # now take care of next 'place'

        return head.next # what we need to return is the whole list
