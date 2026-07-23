class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev=prices[-1]
        ans=0
        for i in range(len(prices)-2,-1,-1):
            if prices[i]>prev:
                prev=max(prev,prices[i])
            elif prices[i]<prev:
                ans+=prev-prices[i]
                prev=prices[i]
        return ans
        