class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[float(inf)]*(m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i]=i
        for i in range(n+1):
            dp[i][0]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[n][m]
        """
        Resursion
        dp=[[float(inf)]*m for _ in range(n)]
        def find(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j]!=float('inf'):
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j]=find(i-1,j-1)
                return dp[i][j]
            dp[i][j]=min(1+find(i,j-1),1+find(i-1,j-1),1+find(i-1,j))
            return dp[i][j]
        return find(n-1,m-1)
        """    