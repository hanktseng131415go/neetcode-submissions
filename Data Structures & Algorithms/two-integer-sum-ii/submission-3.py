class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # def brute_force():
        #     # time: n**2
        #     # space: 1
        #     for i, m in enumerate(numbers):
        #         dif = target - m
        #         for j, n in enumerate(numbers):
        #             if j == i:
        #                 continue
                    
        #             if n == dif:
        #                 return [i+1, j+1]
            
        # return brute_force()

        def two_pointers():
            l, r = 0, len(numbers)-1
            while l < r:
                s = numbers[l] + numbers[r]
                if s > target:
                    r-=1
                elif s < target:
                    l+=1
                else:
                    return [l+1, r+1]
            
            return []
        
        return two_pointers()