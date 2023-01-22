class Solution:
    
    def __init__(self):
        self.result = collections.defaultdict(list)
        
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        if s in self.result: 
            return self.result[s] 
        output = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  
                for suf in self.partition(s[i:]):  
                    output.append([s[:i]] + suf)
        self.result[s] = output
        return output