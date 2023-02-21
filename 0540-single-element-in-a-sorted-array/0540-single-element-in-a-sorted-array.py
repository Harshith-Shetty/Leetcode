class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            a = mid % 2 == 0 and nums[mid] == nums[mid - 1]
            b = mid % 2 != 0 and nums[mid] == nums[mid + 1]
            if a or b:
                end = mid - 1
            else: 
                start = mid + 1
        return nums[start - 1]