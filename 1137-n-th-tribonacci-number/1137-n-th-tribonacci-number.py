class Solution:
    dict = {0:0,1:1,2:1}
    def tribonacci(self, n: int) -> int:
        if n<3:
            return self.dict[n]
        elif n in self.dict:
            return self.dict[n]
        self.dict[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return self.dict[n]