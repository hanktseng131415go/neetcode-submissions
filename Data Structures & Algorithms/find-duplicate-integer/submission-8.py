class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Negative Marking
        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0:
                return abs(n)
            
            nums[index] *= -1
        
        # floyd's cycle linked list
        # time: n
        # space: 1
        # slow, fast = 0, 0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        
        # slow2 = 0
        # while True:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]
        #     if slow == slow2:
        #         return slow