from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n=len(grid)
        m=len(grid[0])
        health -= grid[0][0]
        if health <= 0:
            return False
        flag=[[-1]*m for _ in range(n)]
        flag[0][0]=health
        q=deque()
        q.append((0,0,health))
        row_possible=[-1,0,+1,0]
        col_possible=[0,+1,0,-1]
        ans=0
        while q:
            row,col,k=q.popleft()
            if row==n-1 and col==m-1:
                return True
            for i in range(4):
                new_row=row+row_possible[i]
                new_col=col+col_possible[i]
                if 0<=new_row<n and 0<=new_col<m:
                    nh=k-grid[new_row][new_col] 
                    if (nh>0 and (flag[new_row][new_col]==-1 or nh>flag[new_row][new_col])):
                        flag[new_row][new_col]=nh
                        q.append((new_row,new_col,nh))
        return False