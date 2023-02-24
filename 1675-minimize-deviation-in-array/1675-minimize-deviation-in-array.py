class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_odd = 0
        for i in nums:
            while i%2==0:i = i//2
            max_odd = max(max_odd, i)
            
        # step 2: calculating the [(xi, yi)] list
        dev = []
        for i in nums:
            if i%2 == 1:
                if 2*i>max_odd:
                    dev.append((2*i-max_odd, max_odd-i))
                else:
                    dev.append((float('inf'), max_odd-2*i))
            else:
                if i < max_odd:
                    dev.append((float('inf'), max_odd-i))
                else:
                    while i%2==0 and i>max_odd:
                        i = i//2
                    if i < max_odd:
                        dev.append((2*i-max_odd, max_odd-i))
                        
        # step 3: minimal sum of picked xi's and yi's
        dev.sort(reverse=True)
        if not dev: return 0
        max_down = [0] * len(dev)
        cur = 0
        for i in range(len(max_down)):
            cur = max(cur, dev[i][1])
            max_down[i] = cur
        mm = min(max_down[-1], dev[0][0])
        for i in range(len(max_down)-1):
            mm = min(mm, max_down[i]+dev[i+1][0])
        return mm