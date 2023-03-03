class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_pointer = 0
        n_pointer = 0
        while h_pointer < len(haystack):
            if haystack[h_pointer] == needle[0]:
                compare = haystack[h_pointer :h_pointer + len(needle)]
                if compare == needle:
                    return h_pointer

            h_pointer+=1
        return -1