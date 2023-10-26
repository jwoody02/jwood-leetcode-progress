class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        # helper func
        def isLand(m: int, n: int):
            return isValid(m, n) and grid[m][n] == "1"
        def setToWater(m: int, n: int):
            grid[m][n] = "0"
        def isValid(m: int, n: int):
            return m < len(grid) and m >= 0 and n < len(grid[m]) and n >= 0

        # dfs that takes a coordinate as input
        def dfs(coordinate):
            (x,y) = coordinate
            if isValid(x,y):
                setToWater(x,y)
                if isLand(x + 1, y):
                    dfs((x + 1, y))
                if isLand(x, y + 1):
                    dfs((x, y + 1))
                if isLand(x - 1, y):
                    dfs((x - 1, y))
                if isLand(x, y - 1):
                    dfs((x, y - 1))

        for m in range(len(grid)):
            for n in range(len(grid[m])):
                # call dfs if land
                if isLand(m,n):
                    num_islands += 1

                    # the goal of dfs here is to find the connected land
                    # and set it to water(0) so we can keep track of the islands
                    dfs((m,n)) 

        return num_islands