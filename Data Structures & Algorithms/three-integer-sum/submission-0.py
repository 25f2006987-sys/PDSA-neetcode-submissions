class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        out = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pointer1 = i + 1
            pointer2 = n - 1
            while pointer1 < pointer2:
                total = nums[i] + nums[pointer1] + nums[pointer2]
                if total == 0:
                    out.append([nums[i], nums[pointer1], nums[pointer2]])
                    pointer1 += 1
                    pointer2 -= 1
                    while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 - 1]:
                        pointer1 += 1
                    while pointer1 < pointer2 and nums[pointer2] == nums[pointer2 + 1]:
                        pointer2 -= 1
                elif total < 0:
                    pointer1 += 1
                else:
                    pointer2 -= 1
        return out