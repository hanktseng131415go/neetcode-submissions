class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out, queue = [], []
        nums.sort()
        
        def k_sum(k, l, s):
            if k != 2:
                for i in range(l, len(nums) - k + 1):
                    if i > l and nums[i-1] == nums[i]:
                        continue

                    queue.append(nums[i])
                    k_sum(k-1, i+1, s - nums[i])
                    queue.pop()
            
            else:
                ll, rr = l, len(nums)-1
                
                while ll < rr:
                    ss = nums[ll] + nums[rr]
                    if ss > s:
                        rr-=1
                    elif ss < s:
                        ll+=1
                    else:
                        out.append(queue+[nums[ll], nums[rr]])
                        ll+=1
                        rr-=1
                        while ll < rr and nums[ll-1] == nums[ll]:
                            ll+=1
                        while ll < rr and nums[rr] == nums[rr+1]:
                            rr-=1
                
                return
        
        k_sum(4, 0, target)
        return out
        