class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(p)
        alphaS,alphaP=[0]*26,[0]*26
        for x in p:
            alphaP[ord(x)-ord('a')]+=1  
        ans=[]
        for i in range(len(s)):
            alphaS[ord(s[i])-ord('a')]+=1
            if i>=n:
                alphaS[ord(s[i-n])-ord('a')]-=1
            if alphaS==alphaP:
                ans.append(i-n+1)
        return ans
        