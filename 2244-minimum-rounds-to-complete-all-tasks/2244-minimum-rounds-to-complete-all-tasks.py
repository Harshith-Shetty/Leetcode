class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        C=Counter(tasks).values() 
        return sum([ceil(c/3) for c in C if c>1]) if 1 not in C else -1