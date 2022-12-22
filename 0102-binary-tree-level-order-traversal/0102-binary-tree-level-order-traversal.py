# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if(not root):
            return ans
        queue = []
        queue.append(root)
        while (queue):
            list = []
            for x in range(len(queue)):
                if(queue[0].left):
                    queue.append(queue[0].left)
                if(queue[0].right):
                    queue.append(queue[0].right)
                list.append(queue[0].val)
                queue.pop(0)
            ans.append(list)
        return ans
                
        