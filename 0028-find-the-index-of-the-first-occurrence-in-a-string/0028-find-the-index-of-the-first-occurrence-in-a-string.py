class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        first_element_of_needle=needle[0]
        for i in range(h-n+1):
            if haystack[i]==first_element_of_needle and haystack[i:i+n]==needle:
                return i
        return -1