class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:
            return matrix[0][0]
        m=len(matrix[0])
        prev=matrix[0]
        for i in range(1,n):
            cur=[0]*m
            for j in range(m):
                val=float('inf')
                if j==0:
                    val=min(prev[j],prev[j+1])
                elif j==m-1:
                    val=min(prev[j],prev[j-1])
                else:
                    val=min(prev[j],prev[j-1],prev[j+1])
                cur[j]=val+matrix[i][j]
            prev=cur
        return min(prev)