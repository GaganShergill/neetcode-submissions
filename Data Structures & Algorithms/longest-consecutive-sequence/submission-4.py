class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = streak = 0
        nums.sort() # -1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9
        i = j = 0
        curr = nums[i]
        while j < len(nums):
            if nums[j] != curr:
                streak = 0
                i = j
                curr = nums[i]
            while j+1 < len(nums) and nums[j+1] == curr:
                j += 1
            curr += 1
            j += 1
            streak += 1
            res = max(res, streak)
        return res
            