class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        h_map = {}
        for s in strs:
            h_array = [0]*26
            for s_i in s:
                h_array[ord(s_i) - ord('a')] += 1
            
            str_h_array = str(h_array) 
            if str_h_array not in h_map:
                h_map[str_h_array] = []
            
            h_map[str_h_array].append(s)
        
        output = []
        for k in h_map:
            output.append(h_map[k])
        
        return output
            
