class Solution:
    def isValid(self, s: str) -> bool:
        
        stack  = []

        hashmap = { ")":"(", "]":"[","}":"{"}

        for i in range(len(s)):

            if s[i] in hashmap.values():
                stack.append(s[i])

            elif not stack:
                return False

            elif stack.pop()!=hashmap[s[i]]:

                return False

        return len(stack) == 0

        
            