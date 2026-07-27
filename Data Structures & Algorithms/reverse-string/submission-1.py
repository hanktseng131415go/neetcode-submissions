class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # def two_pointers():
        #     # time = n
        #     # space = 1
        #     l, r = 0, len(s)-1
        #     while l <= r:
        #         tmp = s[l]
        #         s[l] = s[r]
        #         s[r] = tmp
        #         l+=1
        #         r-=1
        
        # two_pointers()

        # s.reverse()
        # # time = n
        # # space = 1

        def stack():
            array = []
            for s_i in s:
                array.append(s_i)
            
            i = 0
            while array:
                s[i] = array.pop()
                i+=1
        
        stack()
