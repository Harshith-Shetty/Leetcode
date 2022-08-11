"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        if not root: 
            return ret
        stack = [root]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            stack += node.children[::-1]
        return ret
        