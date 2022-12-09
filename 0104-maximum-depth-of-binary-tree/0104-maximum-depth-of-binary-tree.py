# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxheight = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def check(root,value):
            if(root):
                value = value +1
                self.maxheight = max(value,self.maxheight)
                check(root.left,value)
                check(root.right,value)
        check(root,0)
        return self.maxheight
        