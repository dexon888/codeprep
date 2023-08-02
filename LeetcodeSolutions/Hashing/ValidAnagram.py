def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_count, t_count = {}, {}
        if (len(s) != len(t)): return False

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        return s_count == t_count

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))