class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r,count = 0,0,0
        while l<len(s) and r<len(t):
            if s[l] == t[r]:
                l +=1
                count +=1
            r +=1
        return count == len(s)
        