class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        rsum = 0
        for x,y in enumerate(nums):
            rsum +=y
        for x in range(len(nums)):
            rsum -=nums[x]
            if(lsum == rsum):
                return x
            lsum +=nums[x]
        return -1

            