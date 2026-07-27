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

        # def two_pointers():
        #     # time=n
        #     # space=n
        #     l, r = 0, len(s) - 1
        #     while l <= r:
        #         if s[l]!=s[r]:
        #             s_l, s_r = s[l+1:r+1], s[l:r]
        #             return s_l == s_l[::-1] or s_r == s_r[::-1]

        #         l+=1
        #         r-=1

        #     return True
        
        # return two_pointers()

        def palindrome(l, r, s):
            # l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
            
                l+=1
                r-=1
            
            return True

        def two_pointers_1():
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return palindrome(l+1, r, s) or palindrome(l, r-1, s)

                l+=1
                r-=1
            
            return True

        return two_pointers_1()


