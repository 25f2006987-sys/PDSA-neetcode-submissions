class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        out=[0]*n
        out1=[]
        for i in nums:
            if 1<= i <=n:
                out[i-1]=1
        for i in range(len(out)):
            if out[i]==0:
                out1.append(i)
        if out1:
            return out1[0]+1
        else:
            return n+1
            