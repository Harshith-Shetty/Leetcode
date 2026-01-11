# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursiveInorder(self, root, arr):
        if root is None:
            return
        self.recursiveInorder(root.left, arr)
        arr.append(root.val)
        self.recursiveInorder(root.right, arr)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        self.recursiveInorder(root, arr)
        return arr