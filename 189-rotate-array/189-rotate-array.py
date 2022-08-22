class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        count, start = 0, 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while 1:
                current = (current + k) % len(nums)
                temp, nums[current] = nums[current], prev
                prev = temp
                count += 1
                if start == current:
                    break
            start += 1
            

        