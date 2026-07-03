class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # following Dutch Algo in which
        # 0 to low-1 are all 0's
        # low to mid-1 are all 1's
        # mid to high-1 are mixed elements of 0 1 2
        # high to n-1 are all 2's

        low=mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        