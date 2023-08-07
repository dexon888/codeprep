def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        hashset = set()
        length = 0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            length = max(length, right - left + 1)
            right += 1
        return length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))