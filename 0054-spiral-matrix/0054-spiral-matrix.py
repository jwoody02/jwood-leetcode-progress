class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        
        m, n = len(matrix), len(matrix[0]) # size of matrix
        x, y = 0, 0                        # pointers to current location
        dx, dy = 0, 1                      # change in x, change in y
        spiral_order_list = []             # return array

        # keep track of visited items by changing them to *
        def markVisited(_x, _y):
            nonlocal matrix
            matrix[_x][_y] = "*"
        def isVisited(_x, _y) -> bool:
            nonlocal matrix
            return matrix[_x][_y] == "*"
        def inBounds(_x, _y) -> bool:
            nonlocal m
            nonlocal n
            return 0 <= _x < m and 0 <= _y < n
        
        # iterate thru all items
        for _ in range(m*n):
            # add item to array
            spiral_order_list.append(matrix[x][y])
            markVisited(x,y)
                
            # check if we need to update dx/dy
            if (not inBounds(x+dx,y+dy) or isVisited(x+dx,y+dy)):
                dx, dy = dy, -dx

            # update x,y
            x, y = x + dx, y + dy


        return spiral_order_list