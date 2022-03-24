class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = collections.deque(range(1,n+1))
        while d:
            remain = k -1
            while remain:
                d.append(d.popleft())
                remain -= 1
            ans = d.popleft()
        return ans