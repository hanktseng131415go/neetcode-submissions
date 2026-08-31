class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        out = 0
        while l <= r:
            m = l + (r - l) // 2
            p = m ** 2
            if p < x:
                l = m + 1
                out = m
            elif x < p:
                r = m - 1
            else:
                return m
        
        return out
