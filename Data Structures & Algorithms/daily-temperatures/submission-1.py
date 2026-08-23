class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                past_i, past_t = stack.pop()
                out[past_i] = (i - past_i)
            
            stack.append((i, t))
        
        return out