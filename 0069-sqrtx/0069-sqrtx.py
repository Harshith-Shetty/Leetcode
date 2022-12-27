class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1: 
            return x
        max = x;
        min = 0;
        q = (min+max)//2;
        while(min < max):
            c = q * q;
            if c == x: 
                return q;
            elif c < x: 
                min = q+1;
            else: 
                max=q;
            q=(min+max)//2;
        return q - 1;