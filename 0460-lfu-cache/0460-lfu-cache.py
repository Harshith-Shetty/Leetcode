class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.time = 0
        self.map = {}              
        self.freq_time = {}         
        self.priority_queue = []    
        self.update = set()

    def get(self, key: int) -> int:
        self.time += 1

        if key in self.map:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time) 
            self.update.add(key)
            return self.map[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return 
        self.time += 1
        if not key in self.map:
            if len(self.map) >= self.capacity:    
                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    _, _, k = heapq.heappop(self.priority_queue)
                    f, t = self.freq_time[k]
                    heapq.heappush(self.priority_queue, (f, t, k))
                    self.update.remove(k)
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)
            self.freq_time[key] = (0, self.time)
            heapq.heappush(self.priority_queue, (0, self.time, key))
        else:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time) 
            self.update.add(key)

        self.map[key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)