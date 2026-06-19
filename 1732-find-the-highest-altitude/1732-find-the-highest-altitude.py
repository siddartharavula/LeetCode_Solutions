class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        val,ans=0,0
        for x in gain:
            val+=x
            ans=max(ans,val)
        return ans