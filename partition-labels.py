class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #S = collections.Counter(S)
        x = []
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                x.append(i-anchor +1)
                anchor = i+1
        return x
