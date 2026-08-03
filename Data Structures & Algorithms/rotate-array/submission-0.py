class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def brute_force(k):
            n = len(nums)
            k = k % n
            while k:
                tmp = nums[n-1]
                for i in range(n-1, 0, -1):
                    nums[i] = nums[i-1]
                
                nums[0] = tmp
                k-=1
        
        return brute_force(k)
