# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(root1,root2):
            if root1 == None and root2 == None:
                return True
            if (root1 != None and root2 != None) and (root1.val == root2.val):
                return check(root1.right,root2.left) and check(root1.left,root2.right)
            return False
        return check(root,root)