class Solution:
    def isValid(self, s: str) -> bool:
        parent_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        tmp = []
        for i in s:
            if i in parent_map:
                tmp.append(parent_map[i])
            
            else:
                if tmp and tmp[-1] == i:
                    tmp.pop()
                else:
                    return False
        
        return True if not tmp else False