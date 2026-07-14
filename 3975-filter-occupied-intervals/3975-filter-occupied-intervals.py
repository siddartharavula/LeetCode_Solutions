class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        n=len(occupiedIntervals)
        occupiedIntervals.sort()
        stack=[occupiedIntervals[0]]
        for i in range(1,n):
            prev=stack[-1]
            cur=occupiedIntervals[i]
            if prev[1]>=cur[0] or cur[0]-prev[1]==1:
                stack.pop()
                new_start=min(prev[0],cur[0])
                new_end=max(prev[1],cur[1])
                stack.append([new_start,new_end])
            else:
                stack.append(cur)
        print(stack)
        temp=[]
        for i in range(len(stack)):
            prev=stack[i]
            if prev[1]<freeStart: # before free time
                temp.append(prev) 
            elif prev[0]>=freeStart and prev[1]<=freeEnd: # in-between free time
                continue  
            elif prev[0]>freeEnd: # after free time
                temp.append(prev) 
            elif prev[0]<freeStart and prev[1]>freeEnd: # free time is in-between interval
                start=prev[0]
                end=freeStart-1
                temp.append([start,end])
                start=freeEnd+1
                end=prev[1]
                temp.append([start,end])
            elif prev[0]<freeStart and prev[1]>=freeStart: # starts before but ends in-between free time
                end=freeStart-1
                temp.append([prev[0],end])
            elif prev[0]>=freeStart and prev[1]>freeEnd: # starts in-between buts end after free time
                start=freeEnd+1
                temp.append([start,prev[1]])
        return temp