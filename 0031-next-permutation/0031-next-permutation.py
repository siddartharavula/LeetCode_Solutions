class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        ind=-1
        #finding the break point of the array
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        #if array is always increasing from the end then that means it's the last permutation, return 1st one
        if ind==-1:
            return nums.reverse()
        #swap the ind value with the number which is just greater then that form right of it
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
                
        def rev(i,j):
            if i>j or i==j:
                return
            nums[i],nums[j]=nums[j],nums[i]
            rev(i+1,j-1)

        #reverse it
        rev(ind+1,n-1)
        
        """
        Do not return anything, modify nums in-place instead.
        """
        