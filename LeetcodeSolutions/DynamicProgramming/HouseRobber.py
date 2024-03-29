def rob(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n + 1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
nums = [2,7,9,3,1]
print(rob(nums))