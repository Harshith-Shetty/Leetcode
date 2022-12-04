# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root):
            if not root:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            self.result = max(self.result, left+right)
            return 1+max(right,left)
        diameter(root)
        return self.result