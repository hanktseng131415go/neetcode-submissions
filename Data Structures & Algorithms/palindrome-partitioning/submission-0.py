class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        out = []

        def dfs(cur, i):

            if i >= len(s):
                out.append(cur[:])
                return
            for j in range(i, len(s)):
                if self.pali(s, i, j):
                    cur.append(s[i:j+1])
                    dfs(cur, j+1)
                    cur.pop()

        dfs([], 0)

        return out
    
    def pali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1

        return True