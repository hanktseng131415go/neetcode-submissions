class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        out = [[]]
        def dfs(i, cur):

            if i >= len(nums):
                return 
            
            cur.append(nums[i])
            out.append(cur[:])
            dfs(i+1, cur)
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1, cur)
        
        dfs(0, [])

        return out