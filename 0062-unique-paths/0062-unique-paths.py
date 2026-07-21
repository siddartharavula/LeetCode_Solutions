class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Tabulation
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        
        """
        Memorization
        dp=[[-1]*n for _ in range(m)]
        def find(i,j):
            if i==0 and j==0:
                return 1
            elif i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            left=find(i-1,j)
            right=find(i,j-1)
            dp[i][j]=left+right
            return dp[i][j]
        return find(m-1,n-1)
        """
        
        