class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1=='' and word2=='':
            return ''
        n1, n2= len(word1), len(word2)
        count=0
        sout=''
        while count<n1 and count<n2:
            sout+=word1[count]
            sout+=word2[count]
            count+=1
        if count<n1:
            sout+=word1[count:]
        if count<n2:
            sout+=word2[count:]
        return sout

        