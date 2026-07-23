class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        i=0
        j=(n*m)-1
        while i<=j:
            mid=(i+j)//2
            if matrix[mid//m][mid%m]==target:
                return True
            elif matrix[mid//m][mid%m]<target:
                i=mid+1
            else:
                j=mid-1
        return False