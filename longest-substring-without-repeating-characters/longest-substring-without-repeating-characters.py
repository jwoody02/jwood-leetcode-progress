class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _ret = 0
        for i in range(len(s)):
            pass_str = ""
            _continue = True
            _k = i
            while _continue:
                if  _k == len(s) or s[_k] in pass_str:
                    _continue = False
                else:
                    pass_str +=  s[_k]
                _k += 1
            _ret = max(_ret, len(pass_str))
        return _ret

                