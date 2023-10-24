class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # pointers to the left and right sides
        left = 0
        right = len(numbers) - 1

        # iterate until we've found twosum
        while left < right:
            val_sum = numbers[left] + numbers[right]
            # have we found the numbers to add to target?
            if val_sum == target:
                return [left + 1, right + 1]
            
            # if the sum is less than the target, increase left
            if val_sum < target:
                left += 1
            else:
                right -= 1
        return [-1,-1]
        