class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        s=[]
        for i in range(len(nums2)-1,-1,-1):
            if i==len(nums2)-1:
                hm[nums2[i]]=-1
                s.append(nums2[i])
                continue
            while s and nums2[i]>s[-1]:
                s.pop()
            if not s:
                hm[nums2[i]]=-1
            else:
                hm[nums2[i]]=s[-1]
            s.append(nums2[i])
        ans=[]
        for x in nums1:
            ans.append(hm[x])
        return ans
        