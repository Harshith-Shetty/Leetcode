class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while l < r:
            h = min(height[l], height[r])
            res = max(res,  h * (r - l))
            l = l + (height[l] == h)
            r = r - (height[r] == h)
        return res
        
        