class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        arr = [[] for _ in range(len(nums)+1)]
        for num, freq in cntr.items():
            arr[freq].append(num)
        
        res = []
        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
