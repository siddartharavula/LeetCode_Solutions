class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort()
        prev=intervals[0]
        count=0
        for i in range(1,n):
            cur=intervals[i]
            if cur[0]>=prev[0] and cur[1]<=prev[1]: # if previous interval is big
                count+=1
            elif cur[0]<=prev[0] and cur[1]>=prev[1]: # if current interval is big
                count+=1
                prev=cur
            else:
                prev=cur
        return n-count
