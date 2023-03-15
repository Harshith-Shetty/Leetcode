# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = [root]
        seen_null = False
        
        while queue:
            node = queue.pop(0)
            
            if node is None:
                seen_null = True
                continue
                
            if seen_null:
                return False
            
            queue.append(node.left)
            queue.append(node.right)
            
        return True