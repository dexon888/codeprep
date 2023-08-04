def smallerNumbersThanCurrent(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = sorted(nums)
        map = {}
        result = []

        for index, num in enumerate(temp):
            if num not in map:
                map[num] = index
        result = [map[num] for num in nums]
        return result

nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))