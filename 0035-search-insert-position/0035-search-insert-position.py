class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums) - 1
        while beg <= end:
            mid  = (end + beg)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                end = mid - 1
            else:
                beg = mid + 1
        return beg
