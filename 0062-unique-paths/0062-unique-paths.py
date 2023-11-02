class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:  # Choose the smaller dimension for the DP array
            m, n = n, m

        dp = [1] * m

        for _ in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j - 1]

        return dp[-1]

