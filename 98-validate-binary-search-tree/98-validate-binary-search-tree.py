# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []
        self.inorderT(root, order)
        for i in range(1, len(order)):
            if order[i] <= order[i-1]:
                return False
        return True
    
    def inorderT(self, root, order):
        if root is None:
            return
        self.inorderT(root.left, order)
        order.append(root.val)
        self.inorderT(root.right, order)
        