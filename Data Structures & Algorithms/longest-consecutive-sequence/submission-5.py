class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = streak = i = 0
        nums.sort()

        curr = nums[i]
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            
            streak += 1
            curr += 1
            res = max(res, streak)
        return res
            