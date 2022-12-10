# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_array = []      # To store all the sum of node as we iterate on the tree
        max_product = 0       # To store all the Final Maximum Product
        
        def calsum(root):   # Function to calculate the sum and store it in the ArrayList
            if not root:    # Check whether node exists or not
                return 0
            
            sum = root.val + calsum(root.left) + calsum(root.right)     
            # Sum of node would be equal to (=) 
            # Sum of its value and (+) 
            # Sum of all node upto leaf node on its left and (+)
            # Sum of all node upto leaf node on its right.
            
            sum_array.append(sum)   # Append the sum in the ArrayList
            return sum
            
        total = calsum(root) # Call function to calculate total sum of entire tree
        for x in sum_array: # Iterate through all sums of nodes
            max_product = max((total-x)*x , max_product)
        return max_product % (10 ** 9 + 7)
            
            
            
            