# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]
        self.helper(root1,arr1)
        self.helper(root2,arr2)
        return arr1==arr2
        
    def helper(self,root,arr):
        if root is None:
            return
        if root.left is None and root.right is None:
            arr.append(root.val)
        self.helper(root.left,arr)
        self.helper(root.right,arr)