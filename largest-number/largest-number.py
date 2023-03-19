class Solution:
    from functools import cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:
        def keyfunc(a, b):
            if int(a + b) > int(b + a): return 1
            elif a == b: return 0
            else: return -1

        # convert to string list and sort
        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(keyfunc), reverse = True)

        return str(int(''.join(nums)))
