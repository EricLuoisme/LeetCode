# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#

import queue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    the_queue = queue.Queue(maxsize= n + 1)
    node_cur = head
    while node_cur is not None:
        if the_queue.qsize() == n + 1:
            the_queue.get_nowait()
        the_queue.put(node_cur)
        node_cur = node_cur.next

    if the_queue.qsize() < n + 1:
        return head.next
    elif n == 1:
        node_bf = the_queue.get_nowait()
        node_bf.next = None
    else:
        node_bf = the_queue.get_nowait()
        node_del = the_queue.get_nowait()
        node_bf.next = node_del.next
    return head


head = ListNode(1)
n = 1
print(removeNthFromEnd(head, n))

head = ListNode(1)
head.next = ListNode(2)
n = 1
print(removeNthFromEnd(head, n).val)
