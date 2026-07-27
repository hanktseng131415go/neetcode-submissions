class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        def hashmap():

            cur_sum = 0
            out = 0
            h_map = {0:1}
            for n in nums:
                cur_sum += n
                diff = cur_sum - k

                out += h_map.get(diff, 0)
                h_map[cur_sum] = 1 + h_map.get(cur_sum, 0)

            return out
        
        return hashmap()
