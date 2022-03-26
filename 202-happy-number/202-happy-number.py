class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            total = 0
            for d in str(n):
                total = total + int(d)**2
            n = total
            if n == 1:
                return True
        return False