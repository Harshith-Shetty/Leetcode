class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res
        # res = 0
        # l = 0
        # r = len(height)-1
        # while 1 < r:
        #     h = min(height[l], height[r])
        #     res = max(res,h*(r-1))
        #     l = l + (height[l] == h)
        #     r = r - (height[r] ==h)
        # return res
        
        