class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) == 0 or len(nums)==1):
            return
        start = 0
        end = len(nums)-1
        index = 0
        while(index<=end and start<end):
            if(nums[index]==0):
                nums[index]=nums[start]
                nums[start]=0
                index = index + 1
                start = start + 1
            elif(nums[index]==2):
                nums[index]=nums[end]
                nums[end]=2
                end = end - 1
            else:
                index = index + 1
            
                
        