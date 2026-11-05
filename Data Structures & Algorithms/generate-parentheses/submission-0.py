class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        out = []
        cur = []

        def dfs(open_n, close_n):

            if open_n == close_n == n:
                out.append(''.join(cur))
                return 
            
            if open_n < n:
                cur.append('(')
                dfs(open_n+1, close_n)
                cur.pop()

            if close_n < open_n:
                cur.append(')')
                dfs(open_n, close_n+1)
                cur.pop()

        dfs(0, 0)

        return out