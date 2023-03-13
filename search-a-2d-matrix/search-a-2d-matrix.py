class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            # target is either in l or r row
            if matrix[l][0] <= target and matrix[l][-1] >= target:
                return target in matrix[l]
            if matrix[r][0] <= target and matrix[r][-1] >= target:
                return target in matrix[r]
            
            # check if l or r rows are closer to target value
            if abs(target - matrix[l][-1]) > abs(target - matrix[r][0]):
                # right is closer
                l += 1
            else:
                r -= 1
        return False