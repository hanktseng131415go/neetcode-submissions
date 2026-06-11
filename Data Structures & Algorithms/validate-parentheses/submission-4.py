class Solution:
    def isValid(self, s: str) -> bool:
        parent_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        tmp = []
        for i in s:
            if i in parent_map:
                
                if tmp and tmp[-1] == parent_map[i]:
                    tmp.pop()
                else:
                    return False
            
            else:
                tmp.append(i)
        
        return True if not tmp else False