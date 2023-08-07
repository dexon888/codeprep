from collections import defaultdict
def maximumNumberOfStringPairs(words):
        """
        :type words: List[str]
        :rtype: int
        """
        map = defaultdict(int)
        result = 0
        for word in words:
            if word[::-1] in map:
                result += map[word[::-1]]
            map[word] += 1
        return result

words = ["cd","ac","dc","ca","zz"]
print(maximumNumberOfStringPairs(words))