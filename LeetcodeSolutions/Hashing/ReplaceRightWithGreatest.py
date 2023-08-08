def replaceElements(arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_value = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_value
            max_value = max(temp, max_value)
        return arr

arr = [17,18,5,4,6,1]
print(replaceElements(arr))