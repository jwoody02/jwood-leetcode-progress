class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        boxes = {}

        def getBoxNumber(row, col) -> int:
            if row < 3: 
                if col < 3: return 1
                elif col < 6: return 2 
                else: return 3
            elif row < 6: 
                if col < 3: return 4 
                elif col < 6: return 5
                else: return 6
            else: 
                if col < 3: return 7
                elif col < 6: return 8 
                else: 9

        def isNumber(inp) -> bool:
            return inp != "."
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                current_value = board[i][j]
                if isNumber(current_value):
                    if i not in rows: rows[i] = [current_value]
                    else: 
                        if current_value in rows[i]: return False
                        rows[i] += [current_value]
                    
                    if j not in columns: columns[j] = [current_value]
                    else: 
                        if current_value in columns[j]: return False
                        columns[j] += [current_value]
                    
                    box_num = getBoxNumber(i, j)
                    if box_num not in boxes: boxes[box_num] = [current_value]
                    else: 
                        if current_value in boxes[box_num]: return False
                        boxes[box_num] += [current_value]
        return True


