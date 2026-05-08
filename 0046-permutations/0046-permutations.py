class Solution(object):
    def permute(self, nums):
        ans=[]
        def pairs(idx,nums,ans):
            if idx==len(nums):
                ans.append(nums[:])
                return
            for i in range(idx,len(nums)):
                nums[idx],nums[i]=nums[i],nums[idx]
                pairs(idx+1,nums,ans)
                nums[idx],nums[i]=nums[i],nums[idx]
        pairs(0,nums,ans)
        return ans
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        