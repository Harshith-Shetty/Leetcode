class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # First pass: calculate left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Second pass: calculate right products and multiply with left products
        right_product = 1
        for i in reversed(range(n)):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result