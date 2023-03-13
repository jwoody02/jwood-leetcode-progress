class Solution:
    def isPalindrome(self, x: int) -> bool:
        _index = len(str(x)) // 2 # middle of int
        while _index >= 0:
            if str(x)[_index] == "-" and str(x)[len(str(x)) - 1 - _index] == "-":
                _index -= 1
                continue
            if str(x)[_index] == "-" or str(x)[len(str(x)) - 1 - _index] == "-":
                return False
            _current_digit_lower = int(str(x)[_index])
            _current_digit_upper = int(str(x)[len(str(x)) - 1 - _index])
            if _current_digit_lower != _current_digit_upper:
                return False
            _index -= 1
        return True