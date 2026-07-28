class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # def two_pointer():
        #     # time: n+m
        #     # space: n+m

        #     i, j = 0, 0
        #     out = []
        #     while i < len(word1) and j < len(word2):
        #         out.append(word1[i])
        #         out.append(word2[j])
        #         i+=1
        #         j+=1
            
        #     out.append(word1[i:])
        #     out.append(word2[j:])

        #     return ''.join(out)
        
        # return two_pointer()

        # def two_pointer_1():
        #     # time: m+n
        #     i, j = 0, 0
        #     out = []
        #     n, m = len(word1), len(word2)
        #     while i < n or j < m:
        #         if i < n:
        #             out.append(word1[i])
        #         if j < m:
        #             out.append(word2[j])
        #         i+=1
        #         j+=1
            
        #     return ''.join(out)
        
        # return two_pointer_1()

        def one_pointer():

            m, n = len(word1), len(word2)
            out = []
            for i in range(max(m, n)):
                if i < m:
                    out.append(word1[i])
                if i < n:
                    out.append(word2[i])
            
            return ''.join(out)
        
        return one_pointer()

