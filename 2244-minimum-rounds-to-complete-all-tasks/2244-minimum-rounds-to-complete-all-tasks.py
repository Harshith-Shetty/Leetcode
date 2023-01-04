class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mp={}
        # storing frequency of each element in mp
        for i in tasks:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        cnt=0
        for i in mp:
            f=0
            while mp[i]>3:
                mp[i]-=3
                f=1
                cnt+=1
            if mp[i]==2 or mp[i]==3:
                cnt+=1
            elif f==0:
                return -1
            else:
                cnt+=1
        return cnt