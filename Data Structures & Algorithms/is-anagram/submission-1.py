class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = len(s)
        if l != len(t):
            return False

        countS = {}
        countT = {}
        for i in range(l):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
