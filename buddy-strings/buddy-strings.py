class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # check if they have same characters O(n)
        if sorted(s) != sorted(goal):
            print(s,"!(sorted)=",goal)
            # they don't even have the same characters, return False
            return False
        
        # bruteforce O(n^2)
        # for character in s
        #   |_ for character in s:
        #       |_ swap the two characters and check if equal to goal
        
        
        # Test Example #1
        # s = "ab", goal = "ba"
        # idea 1: loop through s and find the two letters that cause the strings to be different. If there're more than two then we return false, otherwise verify and return true
        
        _differing_letters = {}
        
        # find differing letters, keep track of amount.
        # if _differing_letters[{key}] > 1 and len(_differing_letters) > 1, return false
        # if len(_differing_letters) > 1, return false
        # if swapped letters from _differing_letters in s == goal, return true
        for i in range(len(s)):
            if s[i] != goal[i]:
                _differing_letters.update({s[i] : i})
        
        _different_list = list(_differing_letters.keys())
        if len(_different_list) == 1:
            print("only one different letter")
            return False
        if len(_different_list) == 0:
            # goal and s are the same, check if there's at least one letter 
            # that repeats and we can swap with itself, otherwise return false
            print("s and goal are same")
            if len(set(s)) != len(s):
                # there're some duplicates!
                print("duplicates in string, returning true!")
                return True
            else:
                # no duplicates, although they're the same string nothing can be swapped
                print("no duplicates, returning false")
                return False
            
            
        
        # now swap our letters, return true if equals goal
        _index_1 = _differing_letters[_different_list[0]]
        _index_2 = _differing_letters[_different_list[1]]
        
        # convert to list because strings aren't mutable
        _tmp_list = list(s)
        _tmp_list[_index_1], _tmp_list[_index_2] = _tmp_list[_index_2], _tmp_list[_index_1]
        
        print("checking if", ''.join(_tmp_list), "==", goal)
        return ''.join(_tmp_list) == goal
            
        
        