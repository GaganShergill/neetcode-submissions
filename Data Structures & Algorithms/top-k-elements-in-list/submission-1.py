class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        arr = list(cntr.items())
        arr.sort(key = lambda x: x[1])
        res = []
        while k > 0:
            res.append(arr.pop()[0])
            k -= 1
    
        return res
