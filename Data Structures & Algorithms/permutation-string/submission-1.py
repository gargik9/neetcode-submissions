class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        need = Counter(s1)          # counts we want
        window = Counter(s2[:k])    # counts in the first window

        if window == need:
            return True

        for i in range(k, len(s2)):
            window[s2[i]] += 1      # new char enters on the right
            window[s2[i - k]] -= 1  # old char leaves on the left
            if window[s2[i - k]] == 0:
                del window[s2[i - k]]   # drop zeros so == works
            if window == need:
                return True

        return False