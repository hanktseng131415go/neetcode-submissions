class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack-II
        cur = path.split('/')
        stack = []
        for c in cur:
            if c == '..':
                if stack: stack.pop()
            elif c != '.' and c != '':
                stack.append(c)
        
        return '/' + '/'.join(stack)

        # # stack-I
        # # time: n
        # # space: n
        # stack = []
        # cur = ''
        # for c in path + '/':
        #     if c == '/':
        #         if cur == '..':
        #             if stack: stack.pop()
        #         elif cur != '.' and cur != '':
        #             stack.append(cur)
                
        #         cur = ''
        #     else:
        #         cur += c
        
        # return '/' + '/'.join(stack)