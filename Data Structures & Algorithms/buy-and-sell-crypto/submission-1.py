class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<=1:
            return 0
        out={}
        for i in range(n-1):
            out[i]=max(0,max(prices[i+1:])-prices[i])
        return max(out.values())

        