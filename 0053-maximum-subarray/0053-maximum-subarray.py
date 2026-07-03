class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=0
        final=float('-inf')
        for i in range(len(nums)):
            if ans<0:
                ans=0
            ans+=nums[i]
            final=max(ans,final)
        return final
        