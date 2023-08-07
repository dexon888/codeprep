from collections import Counter
def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        sum = 0
        for num, freq in count.items():
            if freq == 1:
                sum += num
        return sum

nums = [1,2,3,2]
print(sumOfUnique(nums))