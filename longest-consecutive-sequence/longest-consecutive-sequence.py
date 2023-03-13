class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort and remove duplicates
        nums2 = sorted([*set(sorted(nums))])
        ret_val = 0
        _previous = None
        _current_seq_length = 0
        for num in nums2:
            if _previous == None:
                _previous = num
                _current_seq_length = 1
            else:
                if num - 1 == _previous:
                    _current_seq_length += 1
                else:
                    _previous = None
                    if _current_seq_length > ret_val:
                        ret_val = _current_seq_length
                    _current_seq_length = 1
                _previous = num
        if _current_seq_length != 0 and _current_seq_length > ret_val:
            return _current_seq_length
        return ret_val