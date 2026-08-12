class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # def brute_force():
        #     # time: n
        #     # space: 1
        #     n = len(nums)
        #     for l in range(n):
        #         for r in range(l+1, n):
        #             if r - l <= k and nums[l] == nums[r]:
        #                 return True

        #     return False
        
        # return brute_force()

        # def hash_map():
        #     # time: n
        #     # space: n
        #     h_map = {}
        #     n = len(nums)
        #     for i in range(n):
        #         if nums[i] in h_map and i - h_map[nums[i]] <=k:
        #             return True
        #         h_map[nums[i]] = i
            
        #     return False
        
        # return hash_map()

        def hash_set():
            n = len(nums)
            h_set = set()
            l = 0
            for r in range(n):
                while r - l > k:
                    h_set.remove(nums[l])
                    l+=1
                if nums[r] in h_set:
                    return True
                h_set.add(nums[r])
            
            return False

        return hash_set()