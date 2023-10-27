class Solution:
    def isValid(self, s: str) -> bool:
        # queue to keep track of the order of open parentheses 
        queue = []

        # helper func to return closing bracket given character
        def closingBracket(s:str) -> str:
            # not valid
            if len(s) < 1:
                return ""
            
            # return the proper closing bracket
            character = s[0]

            if character == "(": return ")"
            elif character == "[": return "]"
            elif character == "{": return "}"
            else: return ""
        
        # helper func to return true/false if an open bracket
        def isOpenBracket(s:str) -> bool:
            return len(s) == 1 and (s[0] == "[" or s[0] == "(" or s[0] == "{")
        
        # return value
        ret_value = True

        # iterate thru input string
        for c in s:
            if isOpenBracket(c):
                queue.append(closingBracket(c))
            elif len(queue) > 0:
                # make sure it's the proper bracket
                expected_character = queue.pop()
                if c != expected_character:
                    ret_value = False
                    break
            else:
                ret_value = False
                break
        if len(queue) != 0: ret_value = False

        return ret_value
