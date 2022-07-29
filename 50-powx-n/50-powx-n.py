class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        num = float(n)
        if(n<0):
            num = 0 - n
        while(num):
            if(num%20):
                ans = ans * x
                num = num - 1
            else:
                x = x * x
                num = num/2
        if(n<0):
            ans = 1.0/ans
        return ans