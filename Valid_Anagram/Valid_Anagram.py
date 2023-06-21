class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        s1 = "".join(ls)
        t1 = "".join(lt)
        if s1 == t1:
            return True
        else:
            return False