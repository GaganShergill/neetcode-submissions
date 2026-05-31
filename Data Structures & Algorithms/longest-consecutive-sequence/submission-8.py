class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums) # 2, 20, 4, 10, 3, 5
        res = 0
        for num in nums:
            if (num-1) not in myset:
                streak = 1
                while (num+streak) in myset:
                    streak += 1
            
                res = max(res, streak)
        
        return res