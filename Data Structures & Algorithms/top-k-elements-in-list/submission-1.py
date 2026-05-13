class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {}
        for num in nums:
            cnts[num] = 1 + cnts.get(num, 0)

        cnt_lst = []
        for num, cnt in cnts.items():
            cnt_lst.append([cnt, num])
        cnt_lst.sort()

        rs = []
        while len(rs) < k:
            rs.append(cnt_lst.pop()[1])
        
        return rs