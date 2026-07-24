class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        dp=[1]*n
        ap=list(range(n))
        last=0
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1 
                    ap[i]=j
            if dp[i]>dp[last]:
                last=i
        ans=[]
        while last>=0:
            ans.append(nums[last])
            if ap[last]==last:
                break
            last=ap[last]
        ans.reverse() 
        return ans       