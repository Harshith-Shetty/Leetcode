# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return None
        output = []
        def appendstr(root,value):
            if(not root.left and not root.right):
                output.append(value)
            if(root.left):
                appendstr(root.left,value+"->"+str(root.left.val))
            if(root.right):
                appendstr(root.right,value+"->"+str(root.right.val))
            
        appendstr(root,str(root.val))
        return output
        