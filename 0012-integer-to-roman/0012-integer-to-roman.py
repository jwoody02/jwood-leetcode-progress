class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        complete_string = ""

        # iterate thru each value in d
        for val in d:
            complete_string += (num // val) * d[val]
            num %= val
        
        # return complete string
        return complete_string