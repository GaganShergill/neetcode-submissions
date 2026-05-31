class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums) # 2, 20, 4, 10, 3, 5
        res = streak = 0
        for num in nums:
            curr = num
            if curr-1 not in myset:
                streak = 0
                while curr in myset:
                    streak += 1
                    curr += 1
            
            res = max(res, streak)
        
        return res