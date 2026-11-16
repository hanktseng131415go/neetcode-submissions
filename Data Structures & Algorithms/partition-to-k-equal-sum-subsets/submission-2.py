class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # time; k**n
        # space: n
        if sum(nums) % k:
            return False
        
        parts = [0] * k
        nums.sort(reverse=True)
        equal = sum(nums) / k
        if nums[0] > equal:
            return False

        def dfs(i):

            if i >= len(nums):
                return True

            for p in range(k):
                if p > 0 and parts[p] == parts[p - 1]:
                    continue

                if parts[p] + nums[i] <= equal:
                    parts[p] += nums[i]
                    if dfs(i+1):
                        return True
                    parts[p] -= nums[i]

                if parts[p] == 0:
                    break
            
            return False
        
        return dfs(0)