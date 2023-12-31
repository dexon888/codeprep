def kthSmallest(self, root, k):
    n = 0
    curr = root
    stack = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
        curr = curr.right
