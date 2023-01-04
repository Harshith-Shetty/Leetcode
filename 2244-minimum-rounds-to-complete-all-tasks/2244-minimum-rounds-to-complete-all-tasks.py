class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        def tot(count):
            rem = count % 3
            div = count // 3
            
            if rem == 0: return div
            else: return div + 1
        
        d = {}
        for n in tasks:
            d[n] = d.get(n, 0) + 1
            
        ans = 0
        for count in d.values():
            if count == 1: return -1
            ans += tot(count)
            
        return ans