class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # width of the window we should check in s2
        window_width = len(s1)

        # hashmap representation of s1 { letter: # occurances }
        s1_dict = dict(Counter(s1))

        # sliding window to find permutation
        for i in range(len(s2)):
            s2_dict = dict(Counter(s2[i:i+window_width]))
            if s1_dict == s2_dict:
                return True

        # no permutations found
        return False            

            
       