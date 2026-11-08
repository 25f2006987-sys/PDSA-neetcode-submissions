class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        # First find row where it can be found
        left=0
        right=m-1
        while left<=right:
            mid=(left+right)//2
            if matrix[mid][0]<=target<=matrix[mid][n-1]:
                break
            elif matrix[mid][0]<target:
                left=mid+1
            else:
                right=mid-1
        else:
            return False
        #Now search within row found above
        row=mid
        left=0
        right=n-1
        while left<=right:
            mid1=(left+right)//2
            if matrix[row][mid1]==target:
                return True
            elif matrix[row][mid1]<target:
                left=mid1+1
            else:
                right=mid1-1
        return False