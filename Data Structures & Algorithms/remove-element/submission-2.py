class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k+=1
        
        # return k

        # time: n
        # space: 1

        l, r = 0, len(nums)
        while l < r:
            if nums[l] == val:
                r-=1
                nums[l] = nums[r]

            else:
                l+=1
        
        return r