class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        max_length = start = 0
        for x, y in enumerate(s):
            if y in dict and start <=dict[y]:
                start = dict[y] + 1
            else:
                max_length = max(max_length, x-start +1)
                
            dict[y] = x
        return max_length
            
        