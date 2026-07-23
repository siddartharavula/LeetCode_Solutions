class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans=-1
        i=0
        j=len(nums)-1
        while i<=j:
            m=(i+j)//2
            if nums[m]==target:
                ans=m
                break
            elif nums[m]<target:
                i=m+1
            else:
                j=m-1
        return ans        