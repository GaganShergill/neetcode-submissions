class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = cnt = 0
        for num in nums:
            cnt = cnt + 1 if num else 0    
            max_cnt = max(max_cnt, cnt)

        return max_cnt