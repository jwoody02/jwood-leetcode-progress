class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # cache for numbers found
        found_numbers = set()

        # iterate thru each num
        for num in nums:
            if num in found_numbers:
                return True
            found_numbers.add(num)

        # all numbers unique
        return False