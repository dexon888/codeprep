from collections import deque


def maxDepth(self, root):
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def maxDepthBFS(self, root):
    if not root:
        return 0
    q = deque([root])
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


def maxDepthIterative(self, root):
    stack = [[root, 1]]
    result = 0
    while stack:
        node, depth = stack.pop()
        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return result
