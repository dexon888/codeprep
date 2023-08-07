def sortString(s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        
        sorted_list = sorted(list(set(s)))

        result = ""
        while (len(result) < len(s)):
            for item in sorted_list:
                if item in dict and dict[item] != 0:
                    result += item
                    dict[item] -= 1
            for item in sorted_list[::-1]:
                if item in dict and dict[item] != 0:
                    result += item
                    dict[item] -= 1
        return result

s = "aaaabbbbcccc"
print(sortString(s))