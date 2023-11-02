class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       # The result variable will hold the final count of paths
        result = 1

        # Calculate the result using a direct method to avoid overflow
        for i in range(1, min(m, n)):
            result = result * (m + n - 1 - i) // i

        return result

