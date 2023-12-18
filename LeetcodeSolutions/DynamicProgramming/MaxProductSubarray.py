def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Initialize the max product, which is a single element of the contiguous array
        result = max(nums)

        currMin, currMax = 1,1

        for n in nums:
            if n == 0:
                  currMin, currMax = 1,1
                  continue
            #Hold a buffer for currMax, since we're recomputing it after
            temp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            result  = max(currMax, result)
        return result