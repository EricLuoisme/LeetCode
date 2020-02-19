
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # really fast implementation by reversing the linked list
    node_prev = None
    node_cur = head

    while node_cur is not None:
        node_next = node_cur.next
        node_cur.next = node_prev
        node_prev = node_cur
        node_cur = node_next

    new_head = node_prev
    if n == 1:
        return new_head.next
    else:
        prev = new_head
        while n != 0:
            n -= 1
            cur = prev.next
            if n == 0:
                prev.next = cur.next
                return new_head
            else:
                prev = prev.next
