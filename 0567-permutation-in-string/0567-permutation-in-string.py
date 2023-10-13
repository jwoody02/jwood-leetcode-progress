class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # width of the window we should check in s2
        window_width = len(s1)

        # dictionary representation of s1 { letter: # occurances }
        s1_dict = {}
        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1
            
        # iterate thru s2
        for i in range(0, len(s2)):
            # create substring dict
            substring = s2[i:i+window_width]
            substr_dict = {}
            for c in substring:
                substr_dict[c] = substr_dict.get(c, 0) + 1
            
            # compare s1 dict with current substring dict
            similar_letters = 0
            for c, val in substr_dict.items():
                if c in s1_dict and s1_dict[c] == val and substr_dict[c] > 0:
                    substr_dict[c] -= 1
                    similar_letters += 1

            # check if all letters accounted for
            found_permutation = (similar_letters == len(s1_dict))
            if found_permutation:
                return True

        return False