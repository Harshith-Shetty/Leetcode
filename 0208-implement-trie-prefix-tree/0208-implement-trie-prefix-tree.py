class Trie(object):

    def __init__(self):
        self.children = {}
        self.end = False
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node  = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.end = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node  = self
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        if node.end == True :
            return True
        return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node  = self
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)