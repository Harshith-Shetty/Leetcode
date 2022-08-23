class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counter = 0
        length = len(nums)
        while counter < length:
            if(nums[counter]==0):
                nums.pop(counter)
                nums.append(0)
                length -=1
            else:
                counter +=1
        