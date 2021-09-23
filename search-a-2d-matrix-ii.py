# Time Complexity = O(m+n)
# Space Complexity = O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row, column = 0, n-1
        while row < m and column >= 0:
            if target  == matrix[row][column]:
                return True
            elif target > matrix[row][column]:
                row += 1
            else:
                column -= 1
        return False