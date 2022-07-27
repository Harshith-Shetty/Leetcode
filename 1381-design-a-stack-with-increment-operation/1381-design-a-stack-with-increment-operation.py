class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.size=maxSize
    def push(self, x: int) -> None:
        if(len(self.stack)<self.size):
            self.stack.append(x)            
    def pop(self) -> int:
        if(self.stack==[]):
            return -1
        else:
            return self.stack.pop(-1)
    def increment(self, k: int, val: int) -> None:
        i = 0
        for x in range(0,len(self.stack)):
            if(i<k):
                i+=1
                self.stack[x]=self.stack[x]+val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)