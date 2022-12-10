# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output =[]
        def check_inlevel(root,level):
            if root:
                if(len(output)==level):
                    output.append(root.val)
                check_inlevel(root.right,level+1)
                check_inlevel(root.left,level+1)
        
        
        check_inlevel(root,0)
        return output