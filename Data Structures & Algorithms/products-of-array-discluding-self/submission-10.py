class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[1]*n
        prod=1
        pre,post=1,1
        for j in range(n):
            out[j]=pre
            pre=pre*nums[j]
        for j in range(n-1,-1,-1):
            out[j]=out[j]*post
            post=post*nums[j]    
            
        return out