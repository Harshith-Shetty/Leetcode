class MyStack:

    def __init__(self):
        self.Q1=[]
        self.Q2=[]
    def push(self, x: int) -> None:
        self.Q1.append(x)
    def pop(self) -> int:
        last = ''
        length = len(self.Q1)
        for x in range(0,length-1):
            self.Q2.append(self.Q1[x])
        last = self.Q1[length-1]
        self.Q1 = self.Q2
        self.Q2 = []
        return last
    def top(self) -> int:
        return self.Q1[-1]
    def empty(self) -> bool:
        return self.Q1==[]
    
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()