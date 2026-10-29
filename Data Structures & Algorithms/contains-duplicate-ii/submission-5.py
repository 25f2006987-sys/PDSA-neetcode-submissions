class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for right, value in enumerate(nums):
            # Remove the value that is now more than k positions away
            if right > k:
                window.remove(nums[right - k - 1])

            if value in window:
                return True

            window.add(value)

        return False