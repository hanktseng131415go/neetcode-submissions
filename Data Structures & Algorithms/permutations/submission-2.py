class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
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
