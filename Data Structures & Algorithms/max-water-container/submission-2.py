class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa=0
        n=len(heights)
        left=0
        right=n-1
        while left<right:
            a=(right-left)*min(heights[left],heights[right])
            if a>maxa:
                maxa=a
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return maxa