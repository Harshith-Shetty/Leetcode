class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(i) != sorted(i) for i in zip(*strs))