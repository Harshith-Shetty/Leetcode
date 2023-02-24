class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        min_val = float('inf')
        min_deviation = float('inf')
        
        for idx in range(len(nums)):
            if nums[idx] % 2 != 0:
                nums[idx] *= 2
            
            heapq.heappush(heap, -nums[idx])
            min_val = min(min_val, nums[idx])
        
        while heap:
            max_val = heapq.heappop(heap) * -1
            min_deviation = min(min_deviation, max_val-min_val)
            
            if max_val % 2 == 0:
                max_val //= 2
                # after dividing by two, get a number that is less than the current minimum 
                min_val = min(min_val, max_val)
                heapq.heappush(heap, -max_val)
            else:
                #If we continue further, we will find a non-maximum deviation among the pairs of numbers in the array after the transformations
                break
        
        return min_deviation