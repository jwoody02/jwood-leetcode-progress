class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return val
        ret_val = False

        # so we can O(1) retrieval
        wordSet = set(wordDict)

        # index cache/memoisation
        index_cache = {}

        def dfs(index):
            # make it so we can edit ret_val
            nonlocal ret_val
            
            # check if we've already handled index
            if index in index_cache:
                return

            # reached the end
            if index == len(s):
                ret_val = True
                return
            
            # call dfs on valid words
            for i in range(index, len(s) + 1):
                if s[index:i] in wordSet:
                    index_cache[index] = 0
                    dfs(i)
        
        dfs(0)
        return ret_val

