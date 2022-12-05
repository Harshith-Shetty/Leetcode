# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        
        def invert(root):
            if root:
                interval = root.left
                root.left = root.right
                root.right = interval
                invert(root.left)
                invert(root.right)
            return 0
        invert(root)
        return node
    
        