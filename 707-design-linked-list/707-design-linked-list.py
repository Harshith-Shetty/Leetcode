class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >=0 and index < self.length:
            position = self.head
            for x in range(index):
                position = position.next
            return position.data
        else:
            return -1
        
        
    def addAtHead(self, val: int) -> None:
        if self.length ==0:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        self.length += 1
            
    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            node = Node(val)
            self.head = node
            self.tail = node
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.length and index >= 0:
            if index == 0:
                self.addAtHead(val)
            elif index == self.length:
                self.addAtTail(val)
            else:
                curr = self.head
                for _ in range(index-1):
                    curr = curr.next
                node = Node(val)
                tmp = curr.next
                curr.next = node
                node.next = tmp
                self.length += 1 
                
    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and index < self.length:
            curr = self.head
            prev = None
            for _ in range(index):
                prev = curr
                curr = curr.next
            if not prev:
                self.head = self.head.next
            else:
                prev.next = curr.next
                if not curr.next:
                    self.tail = prev

            self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)