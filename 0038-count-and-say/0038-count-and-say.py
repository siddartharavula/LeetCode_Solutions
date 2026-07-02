ans=[""]*31
ans[1]="1"
for i in range(2,31):
    prev=ans[i-1][0]
    count=0
    temp=""
    for x in ans[i-1]:
        if x==prev:
            count+=1
        else:
            temp+=str(count)+prev
            count=1
            prev=x
    temp+=str(count)+prev
    ans[i]=temp

class Solution:
    def countAndSay(self, n: int) -> str:
        return ans[n]
        