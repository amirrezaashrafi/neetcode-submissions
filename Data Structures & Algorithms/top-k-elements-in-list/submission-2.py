class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        heap = list()
        for num, cnt in counts.items():
            heapq.heappush(heap, [cnt, num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        rs = list()
        for i in range(k):
            rs.append(heapq.heappop(heap)[1])

        return rs