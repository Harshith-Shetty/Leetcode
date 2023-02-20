class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for x in range(len(nums)):
            if nums[x] < target:
                index +=1
            elif nums[x] == target:
                return x
            else:
                return index
        return index
                       