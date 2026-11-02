class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum1 = 0
        prefix_counts = {0: 1}
        for num in nums:
            sum1 += num
            if sum1 - k in prefix_counts:
                res += prefix_counts[sum1 - k]
            prefix_counts[sum1] = prefix_counts.get(sum1, 0) + 1
        return res