class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diffs = list(accumulate(sorted(c-r for c,r in zip(capacity,rocks))))
        return bisect_right(diffs, additionalRocks)