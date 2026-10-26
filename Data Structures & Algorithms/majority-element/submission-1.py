class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for k in nums:
            if k in d:
                d[k]+=1
            else:
                d[k]=1
        le=int(len(nums)/2)
        out = [x for x in d.keys() if d[x]>le]
        return(out[0])
             