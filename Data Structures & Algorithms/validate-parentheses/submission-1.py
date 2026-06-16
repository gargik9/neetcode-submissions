class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parantheses_map = {"]":"[","}":"{",")":"("}

        for char in s:

            if char not in parantheses_map.keys():
                stack.append(char)

            else:
                if not stack or stack[-1] != parantheses_map[char]:

                    return False

                stack.pop()

        return not stack

            