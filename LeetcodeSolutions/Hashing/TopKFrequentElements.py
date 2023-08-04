import heapq
from collections import Counter
def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Establish a count for each element in nums
        count = Counter(nums)

        #Use a min heap to keep track of the most frequent elements
        min_heap = []
        heapq.heapify(min_heap)

        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = [i for _, i in min_heap]
        return result

nums, k = [1,1,1,2,2,3], 2
print(topKFrequent(nums, k))