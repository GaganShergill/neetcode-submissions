class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        res = 0

        for num in nums:
            streak = 0
            curr = num
            while curr in myset:
                curr += 1
                streak += 1
            res = max(res, streak)
        return res