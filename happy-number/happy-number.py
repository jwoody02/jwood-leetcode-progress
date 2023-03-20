class Solution:
    def isHappy(self, n: int) -> bool:
        
        # keep track of current sum and sums that have already occured
        _current_sum = n
        _sums = {}

        while _current_sum != 1:
            _digits = [int(x) for x in str(_current_sum)]
            _current_sum = 0

            for digit in _digits:
                _current_sum += pow(digit, 2)
            if _current_sum in _sums:
                return False
            _sums.update({_current_sum: 0})
        return True