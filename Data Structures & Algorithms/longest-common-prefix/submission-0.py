class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        ans = ""

        strs = sorted(strs)

        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[-1][i] == strs[0][i]:
                ans+= (strs[0][i])
            else:
                break

        return ans



