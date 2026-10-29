class Solution:
    def validPalindrome(self, s: str) -> bool:
        #Helper function to check palindrone
        def val_pal(s1):
            n=len(s1)//2
            for i in range(n):
                if s1[i] != s1[-i-1]:
                    return False
            return True
        for i in range(len(s)):
            s2=s[:i]+s[i+1:]
            if val_pal(s2):
                return True
        return False

