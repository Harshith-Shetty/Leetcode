class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0 
        points = sorted(points, key=lambda x:x[1])
        arrowLastHit = -float('inf')
        arrow = 0
        for each in points:
            if each[0] > arrowLastHit:
                arrow += 1
                arrowLastHit = each[1]
        return arrow