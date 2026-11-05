class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d={}
        s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        count=1
        for i in s:
            d[count]=i
            count+=1
        
        out=''
        s=columnNumber
        while s > 0:
            s -= 1
            out = d[(s % 26) + 1] + out
            s = s // 26
        return out
            


