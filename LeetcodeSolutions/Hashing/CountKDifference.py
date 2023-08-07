from collections import defaultdict
def countKDifference(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map = defaultdict(int)
        result = 0
        for num in nums:
            complement = num + k
            neg_complement = num - k
            if complement in map:
                result += map[complement]
            if neg_complement in map:
                result += map[neg_complement]
            map[num] += 1
        return result

nums, k = [3,2,1,5,4], 2
print(countKDifference(nums, k))