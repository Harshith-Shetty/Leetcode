class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_possible = max(2 * i if i % 2 else i for i in nums)
        heap = []
        for i in nums:
            # If it's even, divide by 2 until we reach its odd factor (>= 1);
            # if it's odd, leave as odd original
            odd_min, even_max = i, 2 * i if i % 2 else i
            while odd_min % 2 == 0:
                odd_min //= 2
            heap += [(odd_min, even_max)]
        heapq.heapify(heap)
        max_num = max(heap, key=lambda r:r[0])[0]
        min_deviation = max_possible
        while True:
            min_num, even_max = heapq.heappop(heap)
            min_deviation = min(min_deviation, max_num - min_num)
            if min_num == even_max:
                # Min value can't be increased, so we're done
                return min_deviation
            heapq.heappush(heap, (2 * min_num, even_max))
            max_num = max(max_num, 2 * min_num)