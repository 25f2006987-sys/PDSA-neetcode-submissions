class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1 or x==2:
            return 1
        left = 1
        right = x//2
        while left<= right:
            mid=(left+right)//2
            if mid*mid > x:
                right=mid-1
            elif mid*mid==x:
                return mid
            else:
                left=mid+1
        return left-1

        