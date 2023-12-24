def removeNthFromEnd(self, head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head
    # Initialize the right pointer
    while n > 0 and right:
        right = right.next
        n -= 1

    # Shift both pointers until right is at end and left.next is the node to be removed
    while right:
        left = left.next
        right = right.next

    # Delete
    left.next = left.next.next

    return dummy.next
