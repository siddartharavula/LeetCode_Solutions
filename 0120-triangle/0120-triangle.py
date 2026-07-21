class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1]*n for i in range(n)]
        for i in range(n):
            dp[n-1][i]=triangle[n-1][i]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down=triangle[i][j]+dp[i+1][j]
                diag=triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,diag)
        return dp[0][0]   

        """
        Recursion
        def find(i,j):
            if i==n-1:
                return triangle[i][j]
            down=triangle[i][j]+find(i+1,j)
            diag=triangle[i][j]+find(i+1,j+1)
            return min(down,diag)
        return find(0,0)
        """
        