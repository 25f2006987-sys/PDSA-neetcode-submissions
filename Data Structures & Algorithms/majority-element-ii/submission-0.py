class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for k in nums:
            d[k]=d.get(k,0)+1
        print(d)        
        l=[x for x in d.keys() if d[x]>n//3 ]  
        return l  