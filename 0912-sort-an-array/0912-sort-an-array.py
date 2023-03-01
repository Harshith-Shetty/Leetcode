class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while (nums):
            tmp = heapq.heappop(nums)
            result.append(tmp)
        
        return result