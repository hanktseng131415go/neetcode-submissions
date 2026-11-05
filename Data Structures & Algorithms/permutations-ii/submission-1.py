class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        out = []
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        def dfs(cur):

            if len(cur) == len(nums):
                out.append(cur[:])
                return
            
            for i in count:
                if count[i] > 0:
                    cur.append(i)
                    count[i] -= 1
                    dfs(cur)
                    cur.pop()
                    count[i]+=1
        
        dfs([])

        return out

        # time: n * n!
        # space: n * n!
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