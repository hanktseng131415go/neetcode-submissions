class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 0
        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[l] == nums[r]:
                r+=1
            
            l+=1
        
        return l

        # def two_pointers():
        #     # time: n
        #     # space: 1
        #     l, r = 0, 0
        #     while r < len(nums):
        #         nums[l] = nums[r]
        #         while r < len(nums) and nums[l] == nums[r]:
        #             r+=1
                
        #         l+=1
            
        #     return l
        
        # return two_pointers()

        # def two_pointers_1():
        #     # time: n
        #     # space: 1
        #     l = 1
        #     for r in range(1, len(nums)):
        #         if nums[r-1] != nums[r]:
        #             nums[l] = nums[r]
        #             l+=1
            
        #     return l
        
        # return two_pointers_1()
