class Solution:
    from itertools import combinations
    def maxArea(self, height: List[int]) -> int:
        # return val + left and right pointers
        max_area = 0
        left, right = 0, len(height) - 1

        # sliding window while left index < right
        while left < right:
            # update max area
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            # move sliding window based on which index has smaller value
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area