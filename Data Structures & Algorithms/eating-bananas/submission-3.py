class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1
        while left<=right:
            mid=(left+right)//2
            if sum((p+mid-1)//mid for p in piles)<=h:
                right=mid-1
            else:
                left=mid+1
        return left