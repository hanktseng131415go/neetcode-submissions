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

        # def two_pointers():
        #     l, r = 0, len(numbers)-1
        #     while l < r:
        #         s = numbers[l] + numbers[r]
        #         if s > target:
        #             r-=1
        #         elif s < target:
        #             l+=1
        #         else:
        #             return [l+1, r+1]
            
        #     return []
        
        # return two_pointers()
        out, queue = [], []
        numbers.sort()
        
        
        def k_sum(k, l, s):
            if k != 2:
                for i in range(l, len(numbers) - k + 1):
                    if i > l and numbers[i-1] == numbers[i]:
                        continue

                    queue.append(i+1)
                    k_sum(k-1, i+1, s - numbers[i])
                    queue.pop()
            
            else:
                ll, rr = l, len(numbers)-1
                
                while ll < rr:
                    ss = numbers[ll] + numbers[rr]
                    if ss > s:
                        rr-=1
                    elif ss < s:
                        ll+=1
                    else:
                        out.append(queue+[ll+1, rr+1])
                        ll+=1
                        
                        while ll < rr and numbers[ll-1] == numbers[ll]:
                            ll+=1
                        
                
                return
        
        k_sum(2, 0, target)
        return out[0]
        