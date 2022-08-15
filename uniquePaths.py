class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 >= 0 and j-1 >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i-1 >= 0:
                    dp[i][j] = dp[i-1][j]
                elif j-1 >= 0:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
