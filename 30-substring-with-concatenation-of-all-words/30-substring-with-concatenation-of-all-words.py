class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        make a freq dict of words array
        wordLen = len(words[0])
        totalLen = len(of all words)
        res = []
        l,r = 0, totalLen
        for loop with steps of wordLen on s using l
            r = l + wordLen
            window = s[l:r]
            loop over window with steps of wordLen till totalLen
                check if in freq dic
                    decrement it
            if freq dic values less than equal to 0
                add l in res
            reset freq dic
        return res
        '''
        wordsDic = Counter(words)
        wordLen = len(words[0])
        totalLen = len(words) * wordLen
        res = []
        for l in range(0,len(s)):
            wordsDicCopy = wordsDic.copy()
            r = l+totalLen
            window = s[l:r]
            l2 = 0
            while l2 < totalLen:
                r2 = l2 + wordLen
                #print(window[l2:r2],l2)
                if window[l2:r2] in wordsDic:
                    wordsDic[window[l2:r2]] -= 1
                else:
                    break
                l2 += wordLen
            #print(wordsDic)
            if 0 >= max(wordsDic.values()):
                res.append(l)
            wordsDic = wordsDicCopy
        return res
        '''
        e = set()
        f = set(permutations(words))
        totalLen = len(words[0])*len(words)
        ans = []
        for perm in f:
            e.add(''.join(perm))
        for l in range(len(s)):
            r = l + totalLen
            #print(l,s[l:r])
            if s[l:r] in e:
                ans.append(l)
        return ans
        '''
        