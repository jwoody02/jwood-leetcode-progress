class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n: return 0

        # dp solution:
        # dp[i][j] => the number of unique paths to get to this spot
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                dp[i] += [0]

        # 1 path to the first item
        dp[0][0] = 1

        # iterate thru each item
        for i in range(m):
            for j in range(n):
                # add to number of paths if in bounds
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

        return dp[-1][-1]