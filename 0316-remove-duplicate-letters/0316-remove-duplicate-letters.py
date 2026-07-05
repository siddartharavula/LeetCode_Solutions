class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen=set()
        last_occ={}
        for i in range(len(s)):
            last_occ[s[i]]=i
        stack=[]
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and ord(stack[-1])>ord(s[i]) and last_occ[stack[-1]]>i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)     