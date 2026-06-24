class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (set(s) == set(t) and len(s) == len(t)):
            s_list, t_list = list(set(s)), list(set(t))
            s_count, t_count = [],[]
            for i in s_list:
                s_count.append(s.count(i))
                t_count.append(t.count(i))
            if t_count == s_count:
                return True
            else:
                return False
        else:
            return False