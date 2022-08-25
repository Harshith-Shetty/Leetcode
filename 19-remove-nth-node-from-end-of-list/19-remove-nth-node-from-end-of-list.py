# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        point = head
        length = 0
        while point!=None:
            length+=1
            point = point.next
        if length == n:
            return head.next
        point = head
        count = 1
        while count < length-n:
            count+=1
            point = point.next
        point.next = point.next.next
        return head
        
            
        