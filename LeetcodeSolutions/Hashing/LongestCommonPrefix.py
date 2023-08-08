def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or not word[i] == strs[0][i]:
                    return result
            result += strs[0][i]
        return result

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))