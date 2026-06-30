class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=[]
        ans=[-1]*n
        for i in range(2*n-1,-1,-1):
            while s and nums[i%n]>=s[-1]:
                s.pop()
            if i<n:
                if s:
                    ans[i]=s[-1]
            s.append(nums[i%n])
        return ans
        