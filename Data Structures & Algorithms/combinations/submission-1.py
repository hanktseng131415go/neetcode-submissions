class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        out = []
        def dfs(i, cur):

            if len(cur) == k:
                out.append(cur[:])
                return 
            
            if i > n:
                return 
            
            cur.append(i)
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)
        
        dfs(1, [])

        return out