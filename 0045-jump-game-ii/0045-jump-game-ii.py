class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 0
        last = next = 0
        jump = 1
        for i in range(len(nums)):
            temp = next
            next = max((nums[j]+j for j in range(last, next+1)))
            if next >= len(nums)-1:
                break
            jump += 1
            last = temp

        return jump