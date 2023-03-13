class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        _map = {}
        i=0
        for val in nums:
            if (target-val) in _map:
                # now we need index of this:
                val2 = target-val
                # make sure it's not just the same element
                if nums.index(val2) != i:
                    return [i, nums.index(val2)]
            _map.update({val: 0})
            i+=1
        return []