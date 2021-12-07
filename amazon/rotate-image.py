# Time Complexity = O(m)
# Space Complexity = O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        self.transpose(matrix, n)
        self.reflect(matrix, n)

    def transpose(self, matrix: List[List[int]], n: int) -> None:
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix: List[List[int]], n: int) -> None:
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

# Time Complexity = O(m)
# Space Complexity = O(1)
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for row in range(n // 2):
            for col in range(row, n - row - 1):
                matrix[row][col], matrix[col][n - 1 - row] = matrix[col][n - 1 - row], matrix[row][col]
                matrix[row][col], matrix[n - 1 - row][n - 1 - col] = matrix[n - 1 - row][n - 1 - col], matrix[row][col]
                matrix[row][col], matrix[n - 1 - col][row] = matrix[n - 1 - col][row], matrix[row][col]
