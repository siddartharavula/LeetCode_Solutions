class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        k*=2 # overall we have k*2 buy and sell things
        # 1st base case, if ind==n then 0
        # 2nd base case, if BuySell==k then 0
        dp=[[0]*(k+1) for _ in range(n+1)]
        for ind in range(n-1,-1,-1):
            for BuySell in range(k-1,-1,-1):
                if BuySell%2==0:
                    dp[ind][BuySell]=max(-prices[ind]+dp[ind+1][BuySell+1],dp[ind+1][BuySell])
                else:
                    dp[ind][BuySell]=max(prices[ind]+dp[ind+1][BuySell+1],dp[ind+1][BuySell])
        return dp[0][0]
        