class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # cache with O(1) lookup
        cache = {}

        # iterate and return when numbers found
        for i, num in enumerate(nums):
            # the number we need
            pair_num = target - num
            if pair_num in cache:
                return [i, cache[pair_num]]
            
            # update cache {number: index}
            cache[num] = i

        return [-1,-1]