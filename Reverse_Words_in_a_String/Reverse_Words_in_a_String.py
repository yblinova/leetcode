class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        lst = s.split(' ')
        lst.reverse()
        a = ' '
        s = a.join(lst)
        return s