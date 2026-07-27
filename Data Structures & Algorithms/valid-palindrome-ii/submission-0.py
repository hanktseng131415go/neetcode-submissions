class Solution:
    def validPalindrome(self, s: str) -> bool:

        def brute_force():
            if s == s[::-1]:
                return True
            
            for i in range(len(s)):
                tmp_s = s[:i] + s[i+1:]
                if tmp_s == tmp_s[::-1]:
                    return True
            
            return False
            
        return brute_force()