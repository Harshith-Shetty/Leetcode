# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.stack = []
        while head != None:
            self.stack.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        val = int(random.random() * len(self.stack))
        return self.stack[val]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()