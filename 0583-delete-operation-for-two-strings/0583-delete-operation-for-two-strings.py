class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Find the longest common subsequence
         
        n=len(word1)
        m=len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        temp=dp[n][m] # stores the LCS

        # answer will be addition of no.of deletion from word1 and no.of additions from word2

        return n+m-(2*temp)
        