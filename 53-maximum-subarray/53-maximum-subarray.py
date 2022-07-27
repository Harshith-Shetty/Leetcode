from math import *
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = nums[0]
        for x in range (len(nums)):
            sum = sum + nums[x]
            if(sum > maxsum):
                maxsum = sum
            if(sum < 0):
                sum = 0
        return maxsum
            
        