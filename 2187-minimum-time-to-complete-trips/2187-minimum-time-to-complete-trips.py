class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(t):
            res = 0
            for e in time:
                res += t//e
            return res >= totalTrips
        maxt = max(time)
        left, right = 1, (totalTrips//sum([maxt//e for e in time]) + 1)*maxt
        while left < right:
            m = (left + right)//2
            if check(m):
                right = m
            else:
                left = m + 1
        return left