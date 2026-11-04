class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer=0
        n=len(nums)
        while pointer < n-1:
            if nums[pointer+1]==nums[pointer]:
                nums.pop(pointer)
            else:
                pointer+=1
            n=len(nums)
            print(pointer,n, nums)
        if n>=2 and nums[-1]==nums[-2]:
            nums.pop(-1)
        return len(nums)
        