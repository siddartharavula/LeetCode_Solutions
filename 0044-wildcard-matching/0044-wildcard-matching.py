class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            dp[i][0]=False
        for i in range(1,m+1):
            flag=True
            for ind in range(1,i+1):
                if p[ind-1]!="*":
                    flag=False
                    break
            dp[0][i]=flag
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==p[j-1] or p[j-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=="*":
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
        return dp[n][m]
            


        """
        Recursion
        def find(i,j):
            if i<0 and j<0:
                return True
            if j<0 and i>=0:
                return False
            if i<0 and j>=0:
                for ind in range(j+1):
                    if p[ind]!="*":
                        return False
                return True
            if s[i]==p[j] or p[j]==".":
                return find(i-1,j-1)
            if p[j]=="*":
                return find(i-1,j) or find(i,j-1)
            return False
        return find(n-1,m-1)
        """
        