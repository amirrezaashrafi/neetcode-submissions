class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            cnts = [0] * 26
            for ch in s:
                cnts[ord(ch) - ord("a")] += 1
            
            if tuple(cnts) in res:
                res[tuple(cnts)].append(s)
            else:
                res[tuple(cnts)] = [s]

        return list(res.values()) 