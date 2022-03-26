class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        seen = set()
        while n not in seen:
            seen.add(n)
            digits = list(str(n))
            total = 0
            for d in digits:
                total = total + int(d)**2
            n = total
            if n == 1:
                return True
        return False