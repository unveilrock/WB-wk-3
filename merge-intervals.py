class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]>= intervals[i+1][0]:
                intervals[i+1]=[min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
                intervals[i] = None
        return list(filter(None, intervals))
