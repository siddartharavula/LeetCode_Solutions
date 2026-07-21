class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mod=int(1e9+7)
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    dp[i][j]=1
                else:
                    left=up=0
                    if j>0:
                        left=dp[i][j-1]
                    if i>0:
                        up=dp[i-1][j]
                    dp[i][j]=(left+up)
        return dp[m-1][n-1]

        """
        Recursive Code
        def find(i,j):
            if i==0 and j==0:
                return 1
            elif i<0 or j<0 or obstacleGrid[i][j]==1:
                return 0
            return find(i-1,j)+find(i,j-1)
        return find(m-1,n-1)
        """