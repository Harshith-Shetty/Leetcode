class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(set(nums))!=len(nums)):
            return True
        else:
            return False