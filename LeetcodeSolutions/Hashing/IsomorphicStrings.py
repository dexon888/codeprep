def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict, t_dict = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in s_dict and s_dict[c1] != c2) or (c2 in t_dict and t_dict[c2] != c1):
                return False
            s_dict[c1] = c2
            t_dict[c2] = c1
        return True

s = "paper"
t = "title"
print(isIsomorphic(s, t))