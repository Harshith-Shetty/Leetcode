# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def check(root,dir):
            if root:
                if((not root.left and not root.right) and dir == 1):
                    self.sum = self.sum + root.val
                check(root.left,1)
                check(root.right,0)
        check(root,0)
        return self.sum
                    
        
                
        