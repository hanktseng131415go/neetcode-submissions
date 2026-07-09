class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        output = None
        for n in nums:
            if count == 0:
                output = n
            count += 1 if n == output else -1
        
        return output
        
        # h_map = {}
        # max_c = -float('inf')
        # output = None
        # for n in nums:
        #     h_map[n] = 1 + h_map.get(n, 0)
        #     if h_map[n]> max_c:
        #         output = n
        #     max_c = max(max_c, h_map[n])
        
        # return output
        # # time: n
        # # space: n

