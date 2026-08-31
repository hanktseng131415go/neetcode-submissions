class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            p = m ** 2
            if p < x:
                l = m + 1
            elif x < p:
                r = m - 1
            else:
                return m
        
        return r
