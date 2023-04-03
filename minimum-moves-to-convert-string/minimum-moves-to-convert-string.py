class Solution:
    def minimumMoves(self, s: str) -> int:

        # keep track of current index
        index = 0
        ret_val = 0

        while index < len(s):
            if s[index] == 'X':
                ret_val += 1
                index += 2
            index += 1
        return ret_val