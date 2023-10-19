class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return val
        longest_prefix = ""
        # shortest length of a string in the list
        shortest_length = min([len(x) for x in strs])

        # helper func to check if character is the same at index i for each
        def isValidChar(index: int) -> bool:
            if not strs or not strs[0] or len(strs[0]) < index:
                return False
            
            # the character we expect
            expected_char = strs[0][index]

            # iterate and check each string in list
            for string in strs:
                if string[index] != expected_char:
                    return False
            
            # valid!
            return True

        # iterate until found longest common prefix
        for i in range(shortest_length):
            if not isValidChar(i):
                return longest_prefix
            longest_prefix += strs[0][i]

        # no common prefix
        return longest_prefix