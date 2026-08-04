class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = -float('inf')
        l, r = 0, len(heights)-1
        while l < r:
            tmp = (r - l) * min(heights[l], heights[r])
            water = max(water, tmp)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return water
