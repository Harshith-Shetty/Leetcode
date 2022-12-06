# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output = 0
    def calculate(self, root,low,high):
        if root:
            if(root.val>=low and root.val<=high):
                self.output = self.output + root.val
            self.calculate(root.right,low,high)
            self.calculate(root.left,low,high)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.calculate(root,low,high)
        return self.output
        
        