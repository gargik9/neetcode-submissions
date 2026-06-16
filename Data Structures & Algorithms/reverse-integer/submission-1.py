class Solution:
    def reverse(self, x: int) -> int:
        
        num = abs(x)
        rev = 0

        while num > 0:
            g = num % 10
            rev = rev * 10 + g
            num //= 10

        if rev > 2**31 - 1:
            return 0

        return rev if x > 0 else -rev