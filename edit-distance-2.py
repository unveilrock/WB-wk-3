#dp
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        mat = [[0]*(len2+1)for _ in range(len1+1)]
        
        for i in range(len1+1):
            mat[i][0] = i
        for j in range(len2+1):
            mat[0][j] = j
        
        for i in range(1, len1+1):
            for j in range(1, len2 + 1):
                if word1[i-1]==word2[j-1]:
                    mat[i][j]= mat[i-1][j-1]
                else:
                    mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])+1
        return mat[-1][-1]
