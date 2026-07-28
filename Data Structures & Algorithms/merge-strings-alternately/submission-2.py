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

        def two_pointer_1():
            i, j = 0, 0
            out = []
            n, m = len(word1), len(word2)
            while i < n or j < m:
                if i < n:
                    out.append(word1[i])
                if j < m:
                    out.append(word2[j])
                i+=1
                j+=1
            
            return ''.join(out)
        
        return two_pointer_1()