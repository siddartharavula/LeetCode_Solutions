class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=float('inf')
        if len(strs)==1:
            return strs[0]
        for x in strs:
            m=min(m,len(x))
        ans=""
        for i in range(m):
            flag=True
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[j-1][i]:
                    flag=False
                    break
            if flag:
                ans+=strs[0][i]
            else:
                break
        return ans