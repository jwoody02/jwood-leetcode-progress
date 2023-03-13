class Solution:
    def reverse(self, x: int) -> int:
        ret_str = ""
        if '-' in str(x):
            ret_str="-"
        x_str = str(x).replace("-", "")[::-1]
        
        for i in x_str:
            ret_str=ret_str+i
        if int(ret_str) > pow(2,31) or int(ret_str) < pow(-2,31):
            ret_str="0"
        return int(ret_str)