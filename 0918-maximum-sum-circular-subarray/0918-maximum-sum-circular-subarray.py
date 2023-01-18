class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        # Assume the array is not circular and calculate max sub array sum.
        currentminSum = currentmaxSum = nums[0]
        maxSum = nums[0]
        minSum = nums[0]
        for i in range(1, n):
            currentmaxSum = max(nums[i], nums[i]+currentmaxSum)
            currentminSum = min(nums[i], nums[i]+currentminSum)
            maxSum = max(currentmaxSum, maxSum)
            minSum = min(currentminSum, minSum)          
        circularMaxSum = sum(nums)-minSum
        if circularMaxSum == 0:
            return maxSum
        return max(maxSum, circularMaxSum)
