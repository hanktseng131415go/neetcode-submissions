class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def brute_force(k):
        #     # time: k * n
        #     # space: 1
        #     n = len(nums)
        #     k = k % n
        #     while k:
        #         tmp = nums[n-1]
        #         for i in range(n-1, 0, -1):
        #             nums[i] = nums[i-1]
                
        #         nums[0] = tmp
        #         k-=1
        
        # return brute_force(k)

        # def extra_space():
        #     # time: n
        #     # space: 1
        #     n = len(nums)
        #     tmp = [0] * n
        #     for i in range(n):
        #         tmp[(i+k)%n] = nums[i]
            
        #     nums[:] = tmp
        
        # return extra_space()

        def cyclic_traversal(k):

            n = len(nums)
            k %= n

            def reverse(l, r):
                
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    r-=1
            
            reverse(0, n-1)
            reverse(0, k-1)
            reverse(k, n-1)
        
        return cyclic_traversal(k)




