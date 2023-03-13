class Solution:
    def isValid(self, s: str) -> bool:
        _heap = []

        for character in s:
            if character in "({[":
                _heap.append(character)
            else:
                if len(_heap) == 0:
                    return False
                elif character == "]" and _heap[-1] is not "[":
                    return False
                elif character == ")" and _heap[-1] is not "(":
                    return False
                elif character == "}" and _heap[-1] is not "{":
                    return False
                else:
                    _heap.pop()
        return len(_heap) == 0
