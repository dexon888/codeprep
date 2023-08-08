def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 1:
            return [[1]]
        for i in range(numRows):
            if i == 0:
                prev = [1]
                result.append(prev)
            else:
                curr = [1]
                j = 1
                while j < i:
                    curr.append(prev[j - 1] + prev[j])
                    j += 1
                curr.append(1)
                result.append(curr)
                prev = curr
        return result

print(generate(5))