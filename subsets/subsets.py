class Solution:
    from itertools import combinations
    def subsets(self, nums: List[int]) -> List[List[int]]:
        _subs = []
        _combos = []
        for i in range(len(nums) + 1):
            _combos.append(list(combinations(nums, i)))

        for combo in _combos:
            for subset in combo:
                _subs.append(list(subset))
        return _subs
