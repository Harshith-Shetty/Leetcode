class LRUCache:

    def __init__(self, capacity: int):
        self.dict={}
        self.size=capacity    

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict[key]
            del self.dict[key]
            self.dict[key] = val
            return val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
        if len(self.dict) == self.size:
            del self.dict[next(iter(self.dict.keys()))]
        self.dict[key] = value
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)