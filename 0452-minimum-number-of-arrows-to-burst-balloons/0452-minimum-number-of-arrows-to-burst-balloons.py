class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        intervals = sorted( points, key = lambda x : (x[0], x[1]) )
        overlap_time = intervals[0]
        ans = len(intervals)
        # print(intervals)
        for i, interval in enumerate(intervals[1:]):
            if interval[0] <= overlap_time[1]:
                ans -= 1
                overlap_time = [ max(interval[0], overlap_time[0]) , min(interval[1], overlap_time[1]) ]
            else:
                overlap_time = interval
            # print(overlap_time)
        return ans