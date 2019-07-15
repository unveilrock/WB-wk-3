class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        
        a, b = 0, 0
        while a < len(s) and b < len(t):
            if s[a] == t[b]:
                a += 1
            b += 1
        return a == len(s)
