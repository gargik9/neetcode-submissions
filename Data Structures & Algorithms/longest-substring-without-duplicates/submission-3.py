class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        l = 0
        r = 0

        seen = set()

        for r in range(len(s)):

            # If duplicate, move left pointer
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            # Add current character
            seen.add(s[r])

            # Current window length
            curr_length = r - l + 1

            # Update maximum
            max_length = max(max_length, curr_length)


        return max_length


            





        


        