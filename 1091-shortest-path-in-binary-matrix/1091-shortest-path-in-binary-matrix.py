from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        if n==1 and grid[0][0]==0:
            return 1
        row=[-1,-1,0,+1,+1,+1,0,-1]
        col=[0,+1,+1,+1,0,-1,-1,-1]
        graph=[[float('inf')]*n for _ in range(n)]
        graph[0][0]=1
        q=deque()
        q.append((1,0,0))
        while q:
            dis,nr,nc=q.popleft()
            for i in range(8):
                r=nr+row[i]
                c=nc+col[i]
                if 0<=r<n and 0<=c<n and grid[r][c]==0 and dis+1<graph[r][c]:
                    graph[r][c]=dis+1
                    if r==n-1 and c==n-1:
                        return dis+1
                    q.append((dis+1,r,c))
        return -1
        