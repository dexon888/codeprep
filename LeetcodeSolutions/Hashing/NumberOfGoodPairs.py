from collections import defaultdict
def numIdenticalPairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = defaultdict(list)
        num_pairs = 0
        for index, num in enumerate(nums):
            if num in dict:
                num_pairs += len(dict[num])
            dict[num].append(index)
        return num_pairs

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))