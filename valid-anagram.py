#using sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        #return collections.Counter(s)==collections.Counter(t) #more efficient
