class TrieNode:

    def __init__(self):
        self.child = {}
        self.last = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.child:
                node.child[i] = TrieNode()
            
            node = node.child[i]
        
        node.last = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.child:
                return False
            
            node = node.child[i]
        
        return node.last

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.child:
                return False

            node = node.child[i]
        
        return True
        