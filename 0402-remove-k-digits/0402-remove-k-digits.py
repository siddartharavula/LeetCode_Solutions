class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        if n<=k:
            return "0"
        s=[]
        for i in range(n):
            while s and ((k>0 and int(s[-1])>int(num[i]))):
                s.pop()
                k-=1
            s.append(num[i])
        while k>0:
            s.pop()
            k-=1
        ans=""
        while s:
            ans+=s.pop()
        ans=ans[::-1]
        while ans and ans[0]=="0":
            ans=ans[1::]
        return ans if ans else "0"