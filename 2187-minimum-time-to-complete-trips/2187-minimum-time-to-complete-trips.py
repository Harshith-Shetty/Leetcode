class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, totalTrips * min(time)

        def f(x):
            return sum(x // t for t in time) >= totalTrips

        while lo < hi:
            mid = (lo + hi) // 2
            if not f(mid): lo = mid + 1
            else: hi = mid
        return lo