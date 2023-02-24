class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -((nums[i] << 1) if nums[i] & 1 == 1 else nums[i])

        min_num = -max(nums)
        max_nums = nums
        heapq.heapify(max_nums)

        min_deviation = math.inf
        while True:
            max_num = -max_nums[0]
            deviation = max_num - min_num

            if deviation < min_deviation:
                min_deviation = deviation
                if min_deviation == 0:
                    break

            if max_num & 1 == 1:
                break

            max_num >>= 1
            heapq.heapreplace(max_nums, -max_num)
            if max_num < min_num:
                min_num = max_num

        return min_deviation