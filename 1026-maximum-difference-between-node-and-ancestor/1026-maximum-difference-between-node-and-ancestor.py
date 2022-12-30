# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def getDiffMinMax(root):
            if not root.left and not root.right:  # leaf node
                return 0, root.val, root.val
            elif root.left and not root.right:  # root.right is None
                left_diff, left_min, left_max = getDiffMinMax(root.left)
                diff = max(left_diff, root.val - left_min, left_max - root.val)
                root_min, root_max = min(root.val, left_min), max(root.val, left_max)
            elif root.right and not root.left:  # root.left is None
                right_diff, right_min, right_max = getDiffMinMax(root.right)
                diff = max(right_diff, root.val - right_min, right_max - root.val)
                root_min, root_max = min(root.val, right_min), max(root.val, right_max)
            else:
                left_diff, left_min, left_max = getDiffMinMax(root.left)
                right_diff, right_min, right_max = getDiffMinMax(root.right)
                root_max = max(left_max, right_max, root.val)
                root_min = min(left_min, right_min, root.val)
                diff1 = max(root.val - min(left_min, right_min), max(left_max, right_max) - root.val)
                diff2 = max(left_diff, right_diff)
                diff = max(diff1, diff2)
            return diff, root_min, root_max

        return getDiffMinMax(root)[0]