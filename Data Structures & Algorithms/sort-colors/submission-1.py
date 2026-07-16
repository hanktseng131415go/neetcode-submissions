class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def merge_sort():
        #     # time: nlogn
        #     # space: n
        #     def merge(arr, l, m, r):
        #         left = arr[l:m+1]
        #         right = arr[m+1:r+1]
        #         i, j, k = l, 0, 0
        #         while j < len(left) and k < len(right):
        #             if left[j] <= right[k]:
        #                 arr[i] = left[j]
        #                 j+=1
        #             else:
        #                 arr[i] = right[k]
        #                 k+=1
        #             i+=1

        #         while j < len(left):
        #             arr[i] = left[j]
        #             j+=1
        #             i+=1
                
        #         while k < len(right):
        #             arr[i] = right[k]
        #             k+=1
        #             i+=1

        #     def mergesort(arr, l, r):
        #         if l == r:
        #             return arr

        #         m = (l + r) // 2
        #         mergesort(arr, l, m)
        #         mergesort(arr, m+1, r)
        #         merge(arr, l, m, r)

        #     mergesort(nums, 0, len(nums)-1)

        # return merge_sort()

        def counting_sort():
            # time: n
            # space: 1
            count = [0 for _ in range(3)] 
            for n in nums:
                count[n] += 1

            j = 0
            for i in range(3):
                while count[i]:
                    nums[j] = i
                    count[i] -= 1
                    j+=1
        
        return counting_sort()