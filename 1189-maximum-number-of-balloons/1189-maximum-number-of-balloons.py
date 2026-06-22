class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm={}
        for x in text:
            if x in "balon":
                hm[x]=hm.get(x,0)+1
        ans=hm.values()
        if len(ans)<5:
            return 0
        ans=min(hm.values())
        return min(ans,hm['l']//2,hm['o']//2)