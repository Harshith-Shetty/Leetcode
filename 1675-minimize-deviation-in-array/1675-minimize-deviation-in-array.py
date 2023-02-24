class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):
          nums[i] = -((nums[i] << 1) if nums[i] & 1 == 1 else nums[i])

        minNum = -max(nums)
        maxNums = nums
        heapq.heapify(maxNums)
        minDeviation = math.inf

        # Decrease the current max num and compare the deviation en route
        while True:
          maxNum = -maxNums[0]
          deviation = maxNum - minNum
          if deviation < minDeviation:
            minDeviation = deviation

            # An optional shortcut
            if minDeviation == 0:
              break

          # Can't decrease the max num anymore
          if maxNum & 1 == 1:
            break

          maxNum >>= 1
          heapq.heapreplace(maxNums, -maxNum)
          if maxNum < minNum:
            minNum = maxNum

        return minDeviation