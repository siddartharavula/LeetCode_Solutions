class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        s=[(temperatures[-1],n-1)]
        for i in range(n-2,-1,-1):
            while s and temperatures[i]>=s[-1][0]:
                s.pop()
            if s:
                ans[i]=s[-1][1]-i
            s.append((temperatures[i],i))
        return ans
        