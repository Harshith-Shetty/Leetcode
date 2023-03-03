class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        if n < m:
            return -1
        
        i = 0
        while i <= n - m:
            if haystack[i:i+m] == needle:
                return i
            i += 1
        
        return -1