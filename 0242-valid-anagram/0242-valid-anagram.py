class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t): s, t = t, s
        s_map = {}
        for char in s:
            s_map.update({char: s_map.get(char, 0) + 1})
        
        t_map = {}
        for char in t:
            t_map.update({char: t_map.get(char, 0) + 1})
        
        for char in s:
            if char not in t_map:
                return False
            if s_map[char] != t_map[char]:
                return False
        return True