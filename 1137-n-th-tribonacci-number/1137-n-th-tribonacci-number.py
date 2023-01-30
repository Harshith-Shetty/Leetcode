class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        
        for i in range(2, n):
            t = t0 + t1 + t2
            t2, t1, t0 = t, t2, t1
        
        return t