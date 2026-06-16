class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        m = len(s) - 1
        n = 0

        while n<m:
            t=s[n]
            s[n]=s[m]
            s[m]=t
            n+=1
            m-=1

        