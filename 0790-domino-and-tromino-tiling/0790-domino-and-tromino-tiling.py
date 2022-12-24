class Solution:
    def numTilings(self, n: int) -> int:
        nums = [1, 1, 2]
        if n < 3:
            return n
        for i in range(3, n+1):
            nums = [nums[1], nums[2], nums[2] * 2 + nums[0]]
        return nums[2] % (10 ** 9 + 7)
        