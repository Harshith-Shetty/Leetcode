class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        # We take all even, and biggest odd
        odd = 0
        result = 0
        for v in s_counter.values():
            if v % 2 == 0: result += v
            else:
                odd = 1
                result += (v-1) # We take all events and 1 left over
        
        return result + odd
        