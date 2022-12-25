class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        for i in range(1, n):
            nums[i] += nums[i - 1]

        ans = []
        for x in queries:
            id = bisect.bisect_right(nums, x)
            ans.append(id)

        return ans