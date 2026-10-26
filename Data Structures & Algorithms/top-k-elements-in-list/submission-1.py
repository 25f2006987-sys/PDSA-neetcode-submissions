class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for j in nums:
            if j in d.keys():
                d[j]+=1
            else:
                d[j]=1
        L=list(d.items())
        L.sort(key=lambda x:(-x[1],x[0]))
        out=[]
        for i in range (k):
            out.append(L[i][0])
        return out

        