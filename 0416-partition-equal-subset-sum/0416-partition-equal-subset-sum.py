class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        if total&1==1:
            return False
        t=total//2
        dp=[[False]*(t+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=True
        for i in range(1,n+1):
            ind=i-1
            for j in range(1,t+1):
                not_take=dp[i-1][j]
                take=False
                if nums[ind]<=j:
                    take=dp[i-1][j-nums[ind]]
                dp[i][j]=not_take or take
        return dp[n][t]
        """
        Resursion
        def find(i,t):
            if i<0:
                return False
            if t==0:
                return True
            not_take=find(i-1,t)
            take=False
            if nums[i]>=t:
                take=find(i-1,t-nums[i])
            return not_take or take
        return find(n-1,t)
        """