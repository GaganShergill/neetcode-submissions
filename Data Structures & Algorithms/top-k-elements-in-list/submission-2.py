class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        heap = []
        for num in cntr.keys():
            heapq.heappush(heap, (cntr[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
        
