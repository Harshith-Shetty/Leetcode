class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for x ,y in enumerate(nums):
            if(nums[i]!=y):
                i+=1
                nums[i] = y
        return i+1
        