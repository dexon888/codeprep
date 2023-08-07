def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        currSum = 0
        for n in nums:
                if currSum < 0:
                        currSum = 0
                currSum += n
                maxSum = max(maxSum, currSum)
        return maxSum