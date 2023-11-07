class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        # dp solution where products[i] = products[i-1] * products[i + 1]
        products = []
        prefix = 1

        for i in range(len(nums)):
            products.append(prefix)
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
        
        return products

        
