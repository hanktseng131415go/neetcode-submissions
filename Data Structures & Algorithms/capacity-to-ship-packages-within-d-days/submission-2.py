class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m = l + (r - l) // 2
            day = 1
            cur_weight = 0
            for w in weights:
                if w + cur_weight > m:
                    cur_weight = 0
                    day+=1
                cur_weight += w
            
            if day <= days:
                r = m - 1
            else:
                l = m + 1
        
        return l

