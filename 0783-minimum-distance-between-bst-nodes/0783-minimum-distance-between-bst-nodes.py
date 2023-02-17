# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        stack = []
        prev = None
        mindif = float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            mindif = min(root.val - prev.val, mindif) if prev else mindif
            prev = root
            root = root.right
        return mindif