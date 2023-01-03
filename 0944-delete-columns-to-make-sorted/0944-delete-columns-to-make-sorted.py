class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        count = 0
        
        for i in range(n):
            for j in range(1,m):
                if strs[j][i] < strs[j-1][i]:
                    count += 1
                    break
        
        return count