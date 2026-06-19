class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        res=0

        maintain_set = set()

        for r in range(len(s)):

            while s[r] in maintain_set:
                maintain_set.remove(s[l])
                l+=1

            maintain_set.add(s[r])
            res = max(res, r-l+1)

        return res
        

        


        