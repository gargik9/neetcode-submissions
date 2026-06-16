class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1
        c = 0

        # step 1: skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # step 2: count the last word
        while i >= 0 and s[i] != ' ':
            c += 1
            i -= 1

        return c