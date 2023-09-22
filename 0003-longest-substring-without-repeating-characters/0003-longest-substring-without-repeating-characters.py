class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         # initialize variables
        start = 0
        max_len = 0
        used_char = {}
        
        for i in range(len(s)):
            # if the character has been used before and is within the current substring
            if s[i] in used_char and start <= used_char[s[i]]:
                # update the start index to the next character after the last occurrence of s[i]
                start = used_char[s[i]] + 1
            else:
                # update the maximum length if necessary
                max_len = max(max_len, i - start + 1)
            
            # mark the character as used and record its index
            used_char[s[i]] = i
            
        return max_len

                