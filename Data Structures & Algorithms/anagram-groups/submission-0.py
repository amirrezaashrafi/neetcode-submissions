class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_lst = list()
        ans = list()
        for _str in strs:
            sorted_lst.append(sorted(_str))
        
        for i in range(len(sorted_lst)):
            temp = list()
            for j in range(len(sorted_lst)):
                if sorted_lst[i] == sorted_lst[j]:
                    temp.append(strs[j])
            if temp not in ans:
                ans.append(temp)
        
        return ans
            