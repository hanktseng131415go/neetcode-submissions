class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        cur = []
        def dfs(i):

            if i >= len(nums):
                out.append(cur[:])
                return 
            
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)

            return out
        
        dfs(0)

        return out