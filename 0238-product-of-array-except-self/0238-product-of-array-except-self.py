class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [1]*len(nums)
        result = []
        
        prev  = 1        
        for i in range (len(nums)):
            prev = prev*nums[i]
            left.append(prev)
            
        prev = 1        
        for i in reversed(range(len(nums))):
            prev = prev*nums[i]
            right[i] =prev
            
        for i in range(len(nums)):
            value = 1
            if(i < len(nums)-1):
                value *= right[i+1]
            if(i != 0):
                value *= left[i-1]
            result.append(value)
        return result