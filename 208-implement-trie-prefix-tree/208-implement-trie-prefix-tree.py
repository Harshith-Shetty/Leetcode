class Trie:

    def __init__(self):
        self.end= False
        self.c={}       

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            if w not in node.c:
                node.c[w] = Trie()
            node = node.c[w]
        node.end = True
        
    def prefixnode(self, word):
        node = self
        for w in word:
            if w in word:
                if w not in node.c:
                    return None
            node = node.c[w]
        return node

    def search(self, word: str) -> bool:
        node = self.prefixnode(word)
        if not node:
            return False
        else:
            return True if node.end else False

    def startsWith(self, prefix: str) -> bool:
        node = self.prefixnode(prefix)
        return bool(node)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)