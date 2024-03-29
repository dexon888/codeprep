def invertTree(self, root):
    if not root:
        return None

    # Swap the nodes
    temp = root.left
    root.left = root.right
    root.right = temp

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root
