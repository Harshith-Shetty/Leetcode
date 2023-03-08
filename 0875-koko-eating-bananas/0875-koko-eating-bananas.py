class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sum_, N = sum(piles), len(piles)
        def get_h(k):
            h = 0
            for val in piles:
                h += (val // k)
                if val % k:
                    h += 1
            return h

        k_min, k_max = max(sum_//h,1), min(sum_//(h-N+1)+1, 1_000_000_000)
        l, r = k_min, k_max
        while l < r:
            mid = (l+r) // 2
            if get_h(mid) > h:
                l = mid+1
            else:
                r = mid
        return l