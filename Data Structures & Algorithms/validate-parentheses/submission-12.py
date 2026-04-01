class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False

        bracket_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        if s[0] in bracket_map.values():
            return False

        stack = []

        for bracket in s:
            if bracket in bracket_map.keys():
                stack.append(bracket)
            else:
                if not stack:
                    continue
                if bracket != bracket_map[stack.pop()]:
                    return False
      
        return not stack