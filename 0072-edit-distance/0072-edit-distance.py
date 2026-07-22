class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
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