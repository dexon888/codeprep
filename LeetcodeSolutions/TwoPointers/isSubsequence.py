def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1, t1, = 0, 0

        while not s1 >= len(s) and not t1 >= len(t):
            if s[s1] == t[t1]:
                s1 += 1
            t1 += 1
        return s1 == len(s)

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))