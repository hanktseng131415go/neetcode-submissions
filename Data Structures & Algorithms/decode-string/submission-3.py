class Solution:
    def decodeString(self, s: str) -> str:
        
        # recursion
        self.i = 0
        def recursion():
            out = ''
            k = 0
            while self.i < len(s):
                c = s[self.i]
                if c.isdigit():
                    k = 10 * k + int(c)
                elif c == '[':
                    self.i += 1
                    out += k * recursion()
                    k = 0
                elif c == ']':
                    return out
                else:
                    out += c

                self.i += 1
                
            return out
        
        return recursion()

        # # two stack
        # # time: n+N
        # # space: n+N
        # s_stack, c_stack = [], []
        # cur, k = '', 0
        # for i in s:
        #     if i.isdigit():
        #         k = k * 10 + int(i)
        #     elif i == '[':
        #         s_stack.append(cur)
        #         cur = ''
        #         c_stack.append(k)
        #         k = 0
        #     elif i == ']':
        #         tmp = cur
        #         cur = s_stack.pop()
        #         count = c_stack.pop()
        #         cur += count * tmp
        #     else:
        #         cur += i
        
        # return cur

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
