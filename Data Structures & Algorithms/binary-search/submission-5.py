class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n
        if target > nums[len(nums)-1] or target < nums[0]:
            return -1
        if n==0:
            return -1
        while left<=right:
            mid= (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right =mid-1
         
        
        return -1
