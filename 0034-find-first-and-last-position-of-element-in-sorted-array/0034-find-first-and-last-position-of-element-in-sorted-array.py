class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums):
            i,j=0,len(nums)-1
            ind=-1
            while i<=j:
                mid=(i+j)//2
                if nums[mid]==target:
                    ind=mid
                    j=mid-1
                elif nums[mid]<target:
                    i=mid+1
                else:
                    j=mid-1
            return ind
        def second(nums):
            i,j=0,len(nums)-1
            ind=-1
            while i<=j:
                mid=(i+j)//2
                if nums[mid]==target:
                    ind=mid
                    i=mid+1
                elif nums[mid]<target:
                    i=mid+1
                else:
                    j=mid-1
            return ind
        return [first(nums),second(nums)]
        