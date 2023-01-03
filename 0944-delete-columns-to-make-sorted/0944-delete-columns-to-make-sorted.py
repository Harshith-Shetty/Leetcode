class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        check =0
        for i in range(len(strs[0])):
            stack=[ord(x[i]) for x in strs]
            if stack != sorted(stack):
                check += 1
            
        return check