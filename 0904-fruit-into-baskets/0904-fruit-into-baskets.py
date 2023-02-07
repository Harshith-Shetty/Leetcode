class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 2:
            return 1
        
        mx = 0 
        basket = defaultdict(int)
        l = 0 
        
        for r in range(len(fruits)):
          
            basket[fruits[r]] += 1
    
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
                    
            mx = max(mx, r - l + 1)
            
        return mx
