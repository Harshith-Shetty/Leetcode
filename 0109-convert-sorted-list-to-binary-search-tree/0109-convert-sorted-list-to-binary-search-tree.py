# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        
        while(head):
            nums.append(head.val)
            head = head.next
         
        def sortedArrayToBST(nums):
        
            if nums!=[]:
                half = len(nums)//2
                root = TreeNode(nums[half])
                root.left = sortedArrayToBST(nums[:half])
                root.right = sortedArrayToBST(nums[half+1:])
                return root
            else:
                return None    
        
        return sortedArrayToBST(nums)