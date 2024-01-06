def serialize(self, root):
    result = []

    def dfs(root):
        if not root:
            result.append("N")
        result.append(str(root.val))
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return result


def deserialize(self, data):
    vals = data.split(",")
    self.i = 0

    def dfs():
        if vals[self.i] == "N":
            self.i += 1
            return None
        node = TreeNode(int(vals[self.i]))
        self.i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
