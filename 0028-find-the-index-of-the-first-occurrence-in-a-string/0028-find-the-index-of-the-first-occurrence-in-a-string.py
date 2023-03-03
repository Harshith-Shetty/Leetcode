class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        ind = 0
        for i in range(h - n + 1):
            if needle == haystack[i:i+n]:
                return i
        return -1