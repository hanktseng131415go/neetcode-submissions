class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_l = float('inf')
        tmp_s = 0
        for r in range(len(nums)):
            tmp_s += nums[r]
            
            while tmp_s >= target:
                min_l = min(min_l, r-l+1)
                tmp_s -= nums[l]
                l+=1
            
        return 0 if min_l == float('inf') else min_l
        
