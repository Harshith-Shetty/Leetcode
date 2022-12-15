class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        prev = [0 for i in range(m+1)]
        cur = [0 for i in range(m+1)]
        
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if(text1[ind1-1] == text2[ind2-1]):
                    cur[ind2] = 1 + prev[ind2-1]
                else:
                    cur[ind2] = max(prev[ind2],cur[ind2-1])
            prev = [x for x in cur]
        return prev[m]
        