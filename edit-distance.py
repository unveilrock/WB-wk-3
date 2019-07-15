#recursion+memoization

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i = j = 0
        memo = dict()
        return self.minDistance2(word1, word2, i, j, memo)
    
    def minDistance2(self, word1, word2, index1, index2, memo):
        #base case:
        if index1 == len(word1) and index2 == len(word2):
            return 0
        elif index1 ==len(word1):
            return len(word2)-index2
        elif index2 == len(word2):
            return len(word1)-index1
        if (index1, index2) not in memo:
            if word1[index1] == word2[index2]:
                x = self.minDistance2(word1, word2, index1+1, index2+1, memo)
            else:
                ins = self.minDistance2(word1, word2, index1, index2+1, memo)+ 1
                dele = self.minDistance2(word1, word2, index1+1, index2, memo) +1
                rep = self.minDistance2(word1, word2, index1+1, index2+1, memo)+1
                x = min(ins, dele, rep)
            memo[(index1, index2)] = x
        return memo[(index1, index2)]
