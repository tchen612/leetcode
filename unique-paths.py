# Time Complexity = O(mn)
# Space Complexity = O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]