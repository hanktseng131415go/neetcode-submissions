class Solution:
    def decodeString(self, s: str) -> str:
        
        # two stack
        s_stack, c_stack = [], []
        cur = ''
        k = 0
        for i in s:
            if i.isdigit():
                k = k*10 + int(i)
            elif i == '[':
                s_stack.append(cur)
                cur = ''
                c_stack.append(k)
                k = 0 
            elif i == ']':
                tmp = cur
                cur = s_stack.pop()
                count = c_stack.pop()
                cur += tmp * count
            else:
                cur += i
        
        return cur

        # # one stack
        # # time: n + N**2
        # # space: n + N
        # stack = []
        # for i in s:
        #     if i != ']':
        #         stack.append(i)
        #     else:
        #         tmp = ''
        #         while stack[-1] != '[':
        #             tmp = stack.pop() + tmp
        #         stack.pop()
                
        #         k = ''
        #         while stack and stack[-1].isdigit():
        #             k = stack.pop() + k
                
        #         stack.append(int(k) * tmp)
        
        # return ''.join(stack)
