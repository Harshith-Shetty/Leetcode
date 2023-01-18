class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # Assume the array is not circular and calculate max sub array sum.
        currentSum = nums[0]
        maxSum = nums[0]
        for i in range(1, n):
            currentSum = max(nums[i], nums[i]+currentSum)
            maxSum = max(currentSum, maxSum)
        currentSum = nums[0]
        minSum = nums[0]
        for i in range(1, n):
            currentSum = min(nums[i], nums[i]+currentSum)
            minSum = min(currentSum, minSum)
        circularMaxSum = sum(nums)-minSum
        if circularMaxSum == 0:
            return maxSum
        return max(maxSum, circularMaxSum)
