class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        # if arr[0]!=1:
        #     return -1
        ans=0
        for x in arr:
            if ans<x:
                ans+=1
        return ans
        