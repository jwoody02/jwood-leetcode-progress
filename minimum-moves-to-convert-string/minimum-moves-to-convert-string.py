class Solution:
    def minimumMoves(self, s: str) -> int:

        # return answer and index
        ans = i = 0

        while i < len(s):
            # if "X" then move forward 3 and add to ans
            if s[i] == "X":
                i += 2
                ans += 1
            
            # add to i either way
            i += 1
        return ans