class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        l = len(senate)
        d = collections.deque(list(senate))
        removeD = 0
        removeR = 0
        sen = d.popleft()
        if sen == 'D':
            removeR += 1
        else:
            removeD += 1
        d.append(sen)
        
        while removeD <= l and removeR <= l:
            sen = d.popleft()
            if sen == 'D' and removeD > 0:
                removeD -= 1
            elif sen == 'R' and removeR > 0:
                removeR -= 1
            elif sen == 'D':
                d.append('D')
                removeR += 1
            elif sen == 'R':
                d.append('R')
                removeD += 1
                
        if removeD > l:
            return 'Radiant'
        else:
            return 'Dire'
                
                