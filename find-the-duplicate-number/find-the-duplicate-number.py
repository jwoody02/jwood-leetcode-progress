class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        # _slow = 0
        # _fast = len(nums) - 1

        # while _fast >= 0:
        #     if nums[_slow] == nums[_fast] and _slow != _fast:
        #         return nums[_slow]
        #     _fast -= 2
        #     _slow += 1
        # return -1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1

