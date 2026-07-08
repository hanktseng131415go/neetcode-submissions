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

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == val:

                nums[l] = nums[r]
                r-=1
            else:
                l+=1
        
        return l
        # time: n
        # space: 1