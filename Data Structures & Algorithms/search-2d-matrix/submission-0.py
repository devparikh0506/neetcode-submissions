class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        row = len(matrix)
        col = len(matrix[0])
        end = (len(matrix) * len(matrix[0])) - 1

        while start <= end:
            mid  = (start + end) // 2

            mid_row = mid // col
            mid_col = mid % col

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                start = mid+1
            else:
                end = mid-1
        return False
