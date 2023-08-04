def arithmeticTriplets(nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        result = 0
        for num in nums:
            if num - diff in nums and num - 2 * diff in nums:
                result += 1
        return result

nums = [0,1,4,6,7,10]
diff = 3
print(arithmeticTriplets(nums, diff))