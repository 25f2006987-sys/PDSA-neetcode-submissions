class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        count=1
        max=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            elif nums[i]==nums[i+1]:
                continue
            else:
                if count>max:
                    max=count
                count=1
        if count>max:
            max=count

        return max
