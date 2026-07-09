class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h_map = {}
        for n in nums:
            if n not in h_map:
                h_map[n] = 1
            else:
                h_map[n] += 1

        max_c = -float('inf')
        max_n = None
        for n, c in h_map.items():
            if c > max_c:
                max_c = max(c, max_c)
                max_n = n
        
        return max_n