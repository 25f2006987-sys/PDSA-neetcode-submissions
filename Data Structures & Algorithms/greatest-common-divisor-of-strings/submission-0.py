class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        n1,n2= len(str1), len(str2)
        if str1+str2!=str2+str1:
            return ""
        else:
            l=math.gcd(n1,n2)
            return str1[0:l]

