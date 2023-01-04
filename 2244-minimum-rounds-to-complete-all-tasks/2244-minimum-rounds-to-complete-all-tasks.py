class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        def tot(n):
            res = n%3
            div = n//3
            if res ==0: return div
            else: return div +1
                
        ans =0
        for count in Counter(tasks).values():
            if count ==1: return -1
            else: ans += tot(count) 
        return ans