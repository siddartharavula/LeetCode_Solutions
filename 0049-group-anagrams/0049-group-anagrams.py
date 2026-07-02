class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        hm={}
        for x in strs:
            key="".join(sorted(x))   # sorted("eat") gives ["a","e","t"]
            if key not in hm:
                hm[key]=[x]
            else:
                hm[key].append(x)
        for key,arr in hm.items():
            ans.append(arr[:])
        return ans