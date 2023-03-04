class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = last = 0
        min_index = max_index = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last = i + 1
                min_index = max_index = -1
                continue
            if num == minK:
                min_index = i
            if num == maxK:
                max_index = i
            if min_index != -1 and max_index != -1:
                count += min(max_index, min_index) - last + 1
        return count