# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None :
            return []
        if root:
            self.stack.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.stack
            
                
        
        