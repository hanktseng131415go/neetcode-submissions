class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        def two_pointer():
            i, j = 0, 0
            out = []
            while i < len(word1) and j < len(word2):
                out.append(word1[i])
                out.append(word2[j])
                i+=1
                j+=1
            
            out.append(word1[i:])
            out.append(word2[j:])

            return ''.join(out)
        
        return two_pointer()