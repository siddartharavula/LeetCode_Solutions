class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm={}
        for x in words:
            hm[x]=hm.get(x,0)+1
        hm=sorted(hm.items(), key=lambda x:(-x[1],x[0]))
        return [x for x,y in hm[:k]]
    