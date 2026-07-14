class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[-1]*(n+1)
        def rob(i):
            if i<0:
                return 0
            elif i==0:
                return nums[0]
            if memo[i]!=-1:
                return memo[i]
            else:
                take=nums[i]+rob(i-2)
                not_take=0+rob(i-1)
                memo[i]=max(take,not_take)
                return memo[i]
        return rob(n-1)
        