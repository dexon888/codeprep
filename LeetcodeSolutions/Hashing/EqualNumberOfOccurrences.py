def areOccurrencesEqual(s):
        """
        :type s: str
        :rtype: bool
        """
        map = {}
        for c in s:
            map[c] = map.get(c, 0) + 1
        if len(set(map.values())) > 1:
            return False
        return True

s = "abacbc"
print(areOccurrencesEqual(s))