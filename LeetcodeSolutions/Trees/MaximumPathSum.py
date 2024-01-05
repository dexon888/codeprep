def maxPathSum(self, root):
    result = [root.val]
    # Returns the max path sum without splitting

    def dfs(root):
        if not root:
            return 0
        leftMax = max(dfs(root.left), 0)
        rightMax = max(dfs(root.right), 0)

        # Compute the max path sum with splitting
        result[0] = max(result[0], leftMax + root.val + rightMax)
        return root.val + max(leftMax, rightMax)
    dfs(root)
    return result[0]
