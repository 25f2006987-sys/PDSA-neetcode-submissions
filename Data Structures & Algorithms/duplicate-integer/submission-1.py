class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=len(list(nums))
        b=len(set(nums))
        return (a!= b)
        