class Solution:
    def reverse(self, x: int) -> int:
        # Example:
        # Input x = 123
        # 123 % 10 = 3
        # 12 % 10 = 2
        # 1 % 10 = 1

        # initialize return val
        ret_val = 0
        index = 0
        isNegative = x < 0
        x = x if x > 0 else -x # make x positive

        # iterate until x == 0
        while x > 0:
            x, remainder = divmod(x, 10)
            ret_val = (ret_val * 10) + remainder
            index += 1

        # fix for negative val
        if isNegative:
            ret_val = -ret_val

        # return 0 if escaped bounds
        return 0 if (ret_val > pow(2, 31) or ret_val < pow(-2,31)) else ret_val