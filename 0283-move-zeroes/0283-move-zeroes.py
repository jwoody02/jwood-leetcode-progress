class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        offset = 0
        for i in range(len(nums) + offset):
            # if nums[i] is 0, delete and append to end
            if not nums[i-offset]:
                del nums[i-offset]
                nums.append(0)
                offset += 1
