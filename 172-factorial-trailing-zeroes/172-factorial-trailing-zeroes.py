class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum = 1
        flag = 0
        value = ''
        step = 0
        N=n
        for x in range(1,N+1):
            sum = sum*x
        value=str(sum)
        for z in value:
            if(z=='0'):
                flag = flag +1
                if(flag>step):
                    step = flag
            else:
                flag = 0
        return step