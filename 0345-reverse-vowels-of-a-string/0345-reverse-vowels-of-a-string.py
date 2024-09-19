class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU") 
        s_list = list(s) 
        
        left = 0 
        right = len(s_list)-1
        
        while left < right:
            
            while left < right and s_list[left] not in vowels:
                left += 1
            
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            
        return ''.join(s_list)
            