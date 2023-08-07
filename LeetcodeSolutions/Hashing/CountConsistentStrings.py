def countConsistentStrings(allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        result = len(words)
        for word in words:
            for c in word:
                if c not in allowed:
                    result -= 1
                    break

        return result

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words))