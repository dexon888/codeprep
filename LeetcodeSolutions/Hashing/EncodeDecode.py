class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = "".join(str(len(word)) + "#" + word for word in strs)
        return result
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        result, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i : j])
            result.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return result

s = Solution()
input = ["lint", "code", "love", "you"]
print(s.encode(input))
print(s.decode(s.encode(input)))