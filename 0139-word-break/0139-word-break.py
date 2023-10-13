class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # so we get O(1) lookup
        wordSet = set(wordDict)
        
        # s = "leetcode", wordDict = ["leet","code"]
        # Dynamic Programming Solution:
        # dp = [false, false, false, True, false, false, false, True] => does the end of a word in the dictionary happen here
        dp = [True] + [False] * len(s)

        # iterate from 0...len(s) + 1 since substring starts at 1
        for i in range(len(s) + 1):
            for j in range(i):
                # valid word
                if s[j:i] in wordSet:
                    # make sure we can get to this word
                    if dp[j]:
                        dp[i] = True
                    
        return dp[-1]

