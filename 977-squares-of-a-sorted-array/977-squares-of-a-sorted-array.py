class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = int(len(nums) - 1)
        left = 0
        counter = right
        output = [0]*len(nums)
        while counter >=0:
            if nums[left] ** 2 > nums[right] ** 2:
                output[counter] = nums[left] ** 2
                left+=1
            else:
                output[counter] = nums[right] ** 2
                right -=1    
            counter -=1                
        return output
        
        
        
        
