from collections import defaultdict;
def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0: 
            return []
        
        result = defaultdict(list)
        for str in strs:
            word = [0] * 26
            for c in str:
                word[ord(c) - ord("a")] += 1
            result[tuple(word)].append(str)
        
        return result.values()

def groupAnagrams2(strs):
     """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
     anagram_map = defaultdict(list)

     for str in strs:
          sorted_word = ''.join(sorted(str))
          anagram_map[sorted_word].append(str)
     return anagram_map.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
print(groupAnagrams2(strs))

     