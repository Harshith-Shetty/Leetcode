# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output =[]
        def check(root):
            if not root:
                output.append("#")
            if root:
                output.append(str(root.val))
                check(root.left)
                check(root.right)
        check(root)
        return ','.join(output)
            
                    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = data.split(",")
        
        def create():
            if node_list:
                value = node_list.pop(0)
                if(value == "#"):
                    return None
                else:
                    node = TreeNode(int(value))
                    node.left= create()
                    node.right = create()
                return node
        
        home = create()
        return home
                
            
        
        
        
        
        
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))