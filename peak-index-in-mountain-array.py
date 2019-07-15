class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i, j = 0, len(A)-1
        while i<=j:
            peak = (i+j) //2
            print('peak = ', peak)
            if A[peak]> A[peak+1] and A[peak]> A[peak-1]:
                return peak
            elif A[peak]< A[peak+1]:
                i=peak+1
            else:
                j=peak-1
