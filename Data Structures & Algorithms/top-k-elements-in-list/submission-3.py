class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        arr = [[] for _ in range(len(nums)+1)]
        print(arr)
        for num, freq in cntr.items():
            arr[freq].append(num)
        
        res = []
        while len(res) < k:
            a = arr.pop()
            while a and len(res) < k:
                res.append(a.pop())
        return res
