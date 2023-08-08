def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in s[::-1]:
            if i == " ":
                if length >= 1:
                    return length
            else:
                length += 1
        return length

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))