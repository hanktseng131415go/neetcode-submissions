class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass
        h_map = {}
        for i, n_i in enumerate(nums):
            candidate = target - n_i
            if candidate in h_map:
                return [h_map[candidate], i]

            h_map[n_i] = i

        # # two pass
        # h_map = {}
        # for i, n_i in enumerate(nums):
        #     h_map[n_i] = i

        # for i, n_i in enumerate(nums):
        #     candidate = target - n_i 
        #     if candidate in h_map and h_map[candidate] != i:
        #         return [i, h_map[candidate]]
