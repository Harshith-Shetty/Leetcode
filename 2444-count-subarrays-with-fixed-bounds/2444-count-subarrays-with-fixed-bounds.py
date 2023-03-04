class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        m = n = h = -1
        for i,a in enumerate(nums):
            if not minK <= a <= maxK: h = i
            if a == minK: m = i
            if a == maxK: n = i
            res += max(0, min(m, n) - h)
        return res