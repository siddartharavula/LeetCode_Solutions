class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        l=r=0
        while r<len(nums)-1:
            """ len(nums)-1 is coz if we reached (n-1)th index thats enough and if r<n-1 only we continue the process """
            fartest=0
            for i in range(l,r+1):
                fartest=max(fartest,i+nums[i])
            l=r+1
            r=fartest
            jumps+=1
        return jumps
        