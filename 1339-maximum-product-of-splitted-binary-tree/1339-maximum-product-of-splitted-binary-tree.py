# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_array = []            
        def calsum(root):   
            if not root: return 0
            sum = root.val + calsum(root.left) + calsum(root.right)     
            sum_array.append(sum)
            return sum
        total = calsum(root) 
        return max((total-x)*x for x in sum_array) % (10 ** 9 + 7)
            
            
            
            