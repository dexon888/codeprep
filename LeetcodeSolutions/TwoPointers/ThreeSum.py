def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum > 0:
                    right -= 1 
                elif curr_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
        return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))