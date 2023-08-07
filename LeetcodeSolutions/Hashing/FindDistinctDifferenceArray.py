
def distinctDifferenceArray(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            prefix = len(set(nums[:i + 1]))
            suffix = len(set(nums[i + 1:]))
            result.append(prefix - suffix)
        return result

nums = [1,2,3,4,5]
print(distinctDifferenceArray(nums))