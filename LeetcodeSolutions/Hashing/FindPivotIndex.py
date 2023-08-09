def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            rightSum = total - leftSum - num
            if leftSum == rightSum:
                return i
            leftSum += num
        return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))