class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in nums]

        # Bruteforce O(n^2):
        # nested for loop 

        # Optimized O(n):
        # [1,2,3,4]
        # step 1 - Do a forward loop and multiply the current num by all previous vals
        # step 2 - do a backward loop that multiplies by current product of everything

        # value to keep track of current product
        _current_product = 1

        for i in range(len(nums)):
            answer[i] = _current_product
            _current_product *= nums[i]
        
        # reset current product
        _current_product = 1
        for i in range(len(nums)):
            answer[len(nums) - 1 -i] *= _current_product
            _current_product *= nums[len(nums) - 1 -i]

        return answer
