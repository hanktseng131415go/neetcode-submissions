class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def sliding_window():
            h_map = {}
            max_w = 0
            l = 0
            for r in range(len(s)):
                h_map[s[r]] = 1 + h_map.get(s[r], 0)
                
                while (r - l + 1) - max(h_map.values()) > k:
                    h_map[s[l]] -= 1
                    l+=1
                
                max_w = max(max_w, r -l + 1)
            
            return max_w
        
        return sliding_window()