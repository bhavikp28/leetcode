class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])

        top, bottom = 0, row-1

        while top <= bottom:
            r = (top+bottom)//2
            if target > matrix[r][-1]:
                top = r+1
            elif target < matrix[r][0]:
                bottom = r-1
            else:
                break

        if not (top <= bottom):
            return False

        l,right = 0, column
        while l <= right:
            m = (l+right)//2
            if target > matrix[r][m]:
                l = m+1
            elif target < matrix[r][m]:
                right = m-1
            else:
                return True
        return False       