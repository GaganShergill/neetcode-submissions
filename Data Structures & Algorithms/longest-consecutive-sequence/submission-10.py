class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = i = 0
        numSet = list(set(nums))
        numSet.sort()
        print(numSet)
        
        while i < len(numSet):
            streak = 0
            curr = numSet[i]

            while i < len(numSet) and numSet[i] == curr:
                i += 1
                streak += 1
                curr += 1
            res = max(res, streak)
        
        return res
            