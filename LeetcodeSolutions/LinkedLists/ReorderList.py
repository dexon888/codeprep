def reorderList(self, head):
    # Find the middle of the list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next  # Middle point
    # Reverse the second half
    slow.next = None
    prev = slow.next
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node

    # Merge the two halves
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
