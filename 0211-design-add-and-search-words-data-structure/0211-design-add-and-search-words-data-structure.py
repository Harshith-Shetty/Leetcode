class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        reduce(lambda a, x: a.children[x], word, self.root).is_end = True

    def search(self, word: str) -> bool:
        def search_(node: Node, i: int) -> bool:
            if i == len(word): return node.is_end
            ch = word[i]
            if ch != '.' and ch not in node.children: return False
            xs = node.children.values() if ch == '.' else (node.children[ch],)
            return any(search_(x, i + 1) for x in xs)
        
        return search_(self.root, 0)

class Node:
    def __init__(self, children: dict = None, is_end: bool = False) -> None:
        self.children = defaultdict(Node) if children is None else children
        self.is_end = is_end

