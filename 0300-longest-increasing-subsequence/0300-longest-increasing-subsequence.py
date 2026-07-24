class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        ans=0
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and 1+dp[j]>dp[i]:
                    dp[i]=dp[j]+1
            ans=max(ans,dp[i])
        return ans 
        
        import bisect # This module can be in sorted arrays
        ans=[nums[0]]
        for i in range(1,n):
            if nums[i]>ans[-1]:
                ans.append(nums[i])
            else:
                ind=bisect.bisect_left(ans,nums[i]) 
                # bisect.bisect_left(array,value) -> returns the 1st index where we can put value in that array
                ans[ind]=nums[i]
        return len(ans)


        """
        Recursion
        def find(i,prev):
            if i<0:
                return 0
            not_take=find(i-1,prev)
            take=0
            if prev==n or nums[i]<nums[prev]:
                take=1+find(i-1,i)
            return max(take,not_take)
        return find(n-1,n)
        """
        