class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        row = len(m)
        col = len(m[0])


        l = 0
        r = row-1
        row_present = -1
        while l<=r:
            mid = (r+l)//2
            if target >= m[mid][0] and target <= m[mid][col-1]:
                row_present = mid
                break
            if target<m[mid][0]:
                r=mid-1
            else:
                l = mid+1
        l=0
        r=col-1
        while l<=r:
            mid = (r+l)//2
            if target == m[row_present][mid]:
                return True
            if target>m[row_present][mid]:
                l=mid+1
            else:
                r=mid-1
        
        return False