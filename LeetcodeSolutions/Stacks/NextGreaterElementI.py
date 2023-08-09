def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Store the mappings of elements to their next greater elements
        nextGreater = {}
        stack = []

        #Iterate through each number in nums2 array, and check if the top of the stack is less than it
        #If it is, we pop it continuously while assigning it to nextGreater
        for num in nums2:
            while stack and num > stack[-1]: 
                nextGreater[stack.pop()] = num
            stack.append(num)
        #If the stack still has elements, assign the remaining to -1 in the map
        while stack:
            nextGreater[stack.pop()] = -1
        #Create the result list for each mapping in nums1
        result = [nextGreater.get(num, -1) for num in nums1]
        return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))