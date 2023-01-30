class Solution:
    def tribonacci(self, n: int) -> int:
        ar = [None]*(n+1)
        
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
    
        ar[0]=0
        ar[1]=1
        ar[2]=1
        
        for i in range(3,n+1):
            ar[i]=ar[i-3]+ar[i-2]+ar[i-1]
            
        return ar[-1] 