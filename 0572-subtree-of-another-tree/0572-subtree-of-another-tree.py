# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None:
            return False
        def isSame(a,b):
            if a==None and b==None:
                return True
            if a==None or b==None:
                return False
            return a.val==b.val and isSame(a.left,b.left) and isSame(a.right,b.right)
        if isSame(root,subRoot)==True:
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)  