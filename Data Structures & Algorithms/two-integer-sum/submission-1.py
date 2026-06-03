class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, n_i in enumerate(nums):
            h_map[n_i] = i

        for i, n_i in enumerate(nums):
            candidate = target - n_i 
            if candidate in h_map and h_map[candidate] != i:
                return [i, h_map[candidate]]
