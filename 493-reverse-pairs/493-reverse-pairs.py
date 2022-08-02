import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        temp = []
        count =0
        
        for x,y in enumerate(nums):
            count += len(temp)-bisect_right(temp, 2*nums[x])
            bisect.insort(temp, nums[x])
        return count
            
        