class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # length of matrix
        n = len(matrix)

        # iterate thru each pixel
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
            # reverse matrix
            matrix[i] = matrix[i][::-1]
            
        

        