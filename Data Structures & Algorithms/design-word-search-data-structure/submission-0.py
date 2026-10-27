class TrieNode:

    def __init__(self):
        self.child = {}
        self.last = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.child:
                node.child[i] = TrieNode()
            
            node = node.child[i]
        
        node.last = True

    def search(self, word: str) -> bool:

        def dfs(j, node):

            for i in range(j, len(word)):
                w = word[i]
                if w == '.':
                    for child in node.child.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if w not in node.child:
                        return False

                    node = node.child[w]
            
            return node.last
        
        return dfs(0, self.root)