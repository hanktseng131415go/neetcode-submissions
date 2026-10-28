class TrieNode:

    def __init__(self):

        self.child = {}
        self.last = False

class Trie:

    def __init__(self):

        self.root = TrieNode()

    def addword(self, word):
        node = self.root
        for i in word:
            if i not in node.child:
                node.child[i] = TrieNode()
            
            node = node.child[i]
        
        node.last = True
        
class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        trie = Trie()
        for d in dictionary:
            trie.addword(d)

        dp = {len(s): 0}

        def dfs(i):

            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)
            node = trie.root
            for j in range(i, len(s)):
                if s[j] not in node.child:
                    break
                
                node = node.child[s[j]]
                if node.last:
                    res = min(res, dfs(j + 1))
            
            dp[i] = res

            return res
        
        return dfs(0)