class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # so we can lookup in O(1)
        wordSet = set(wordDict)

        # keep track of full valid strings
        valid_strings = []

        def dfs(index, words_array):
            # reached the end of s, append new string
            if index == len(s):
                valid_strings.append(" ".join(words_array))

            # call dfs using current words array
            for i in range(index, len(s) + 1):
                if s[index:i] in wordSet:
                    dfs(i, words_array + [s[index:i]])

        dfs(0, [])
        return valid_strings