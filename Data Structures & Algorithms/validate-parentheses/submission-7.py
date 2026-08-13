class Solution:
    def isValid(self, s: str) -> bool:
        parent_map = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        stack = []
        for i in s:
            if i in parent_map:
                stack.append(parent_map[i])
            else:
                if not stack:
                    return False
                p = stack.pop()
                if p != i:
                    return False

        
        return True if not stack else False

