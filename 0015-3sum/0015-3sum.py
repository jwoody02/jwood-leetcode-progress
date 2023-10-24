class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort nums array
        nums.sort()

        # return array
        zero_sum_triplets = []

        for i, num_i in enumerate(nums):
            # we've already covered this number
            if i > 0 and num_i == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            # iterate until we've evaluated all possibilities for num_i
            while l < r:
                threesum = num_i + nums[l] + nums[r]
                if threesum == 0:
                    zero_sum_triplets.append([num_i, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1] and 1 < r:
                        l += 1
                elif threesum < 0:
                    l += 1
                else:
                    r -= 1
        return zero_sum_triplets

            



        

        