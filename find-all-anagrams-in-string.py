#time limit exceeded using sort
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        out=[]
        p = sorted(list(p))
        window = sorted(list(s[:len(p)]))
        
        for i in range(len(s)-len(p)+1):
            if window==p:
                out.append(i)
            window = sorted(list(s[i+1:len(p)+1+i]))
        return out
