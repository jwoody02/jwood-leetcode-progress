class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_map = {}
        for char in s:
            s_map.update({char: s_map.get(char, 0) + 1})
        
        t_map = {}
        for char in t:
            t_map.update({char: t_map.get(char, 0) + 1})
        
        return s_map == t_map