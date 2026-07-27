class Solution:
    def validPalindrome(self, s: str) -> bool:

        # def brute_force():
        #     # time: n**2
        #     # space: n
        #     if s == s[::-1]:
        #         return True
            
        #     for i in range(len(s)):
        #         tmp_s = s[:i] + s[i+1:]
        #         if tmp_s == tmp_s[::-1]:
        #             return True
            
        #     return False
            
        # return brute_force()

        def two_pointers():
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l]!=s[r]:
                    s_l, s_r = s[l+1:r+1], s[l:r]
                    return s_l == s_l[::-1] or s_r == s_r[::-1]

                l+=1
                r-=1

            return True
        
        return two_pointers()