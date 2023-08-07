def longestConsecutive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        hashset = set(nums)
        for num in nums:
            #Check to see if it's the first of a sequence
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                longest = max(longest, length)
        return longest

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))