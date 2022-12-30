class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums, x):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > nums[mid]: 
                    left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(nums, x):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= nums[mid]: left = mid + 1
                else: right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]


