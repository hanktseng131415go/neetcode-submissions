class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_map = {}
        if len(s) != len(t):
            return False
            
        for s_i in s:
            if s_i not in h_map:
                h_map[s_i] = 1
            else:
                h_map[s_i] += 1
        
        for t_i in t:
            if t_i in h_map:
                h_map[t_i] -= 1
                if h_map[t_i] < 0:
                    return False
            else:
                return False
        
        return True