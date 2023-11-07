class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dic = {}
        for char in s:
            dic.update({char: dic.get(char, 0) + 1})
        
        for char in t:
            if char not in dic: return False
            dic.update({char: dic.get(char, 0) - 1})
        
        for val in dic.values():
            if val != 0: return False

        return True