class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(arr) != len(pattern):
            return False
        
        for i in range(len(arr)):
            if pattern.find(pattern[i]) != arr.index(arr[i]):
                return False
        return True