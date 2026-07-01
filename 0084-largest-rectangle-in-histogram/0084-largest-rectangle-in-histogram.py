class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s=[]
        ans=0
        for i in range(len(heights)):
            while s and heights[s[-1]]>heights[i]:
                temp=heights[s.pop()]
                nse=i
                pse=s[-1] if s else -1
                ans=max(ans,temp*(nse-pse-1))
            s.append(i)
        while s:
            temp=heights[s.pop()]
            nse=len(heights)
            pse=s[-1] if s else -1
            ans=max(ans,temp*(nse-pse-1))
        return ans