class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        out = []

        def dfs(cur):
            
            if len(nums) == len(cur):
                out.append(cur[:])
                return 
            
            for i in count:
                if count[i] > 0:
                    cur.append(i)
                    count[i] -=1
                    dfs(cur)
                    cur.pop()
                    count[i] += 1
            
        dfs([])

        return out
        # time: n * n!
        # space: n * n!
        if len(nums) == 0:
            return [[]]
        out = []
        per = self.permute(nums[1:])
        for p in per:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                out.append(p_copy)
        
        return out
