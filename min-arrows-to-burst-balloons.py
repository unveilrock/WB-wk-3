class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)>0:
            points.sort(key=lambda x: x[1])
            arrows=1
            node=points[0][1]
            for point in points:
                if(point[0]>node):
                    node=point[1]
                    arrows+=1

            return arrows
        else:
            return 0
