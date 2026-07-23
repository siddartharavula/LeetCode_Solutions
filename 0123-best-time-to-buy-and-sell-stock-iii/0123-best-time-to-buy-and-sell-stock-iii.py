class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*5 for _ in range(n+1)]
        for ind in range(n-1,-1,-1):
            for BuySell in range(3,-1,-1):
                if BuySell%2==0:
                    dp[ind][BuySell]=max(-prices[ind]+dp[ind+1][BuySell+1],dp[ind+1][BuySell])
                else:
                    dp[ind][BuySell]=max(prices[ind]+dp[ind+1][BuySell+1],dp[ind+1][BuySell])
        return dp[0][0]
        """
        Type 1
        dp=[[[0]*3 for _ in range(2)]for _ in range(n+1)]
        for ind in range(n-1,-1,-1):
            for canBuy in range(2):
                for flag in range(1,3):
                    if canBuy==1:
                        dp[ind][canBuy][flag]=max(-prices[ind]+dp[ind+1][0][flag],dp[ind+1][1][flag])
                    else:
                        dp[ind][canBuy][flag]=max(prices[ind]+dp[ind+1][1][flag-1],dp[ind+1][0][flag])
        return dp[0][1][2]

        Recursion
        def find(ind,canBuy,flag):
            if ind==n:
                return 0
            if flag==0:
                return 0
            if canBuy:
                return max(-prices[ind]+find(ind+1,False,flag),find(ind+1,True,flag))
            else:
                return max(prices[ind]+find(ind+1,True,flag-1),find(ind+1,False,flag))
        return find(0,True,2)
        """
        