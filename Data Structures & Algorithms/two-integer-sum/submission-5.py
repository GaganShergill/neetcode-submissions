class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, num in enumerate(nums):
            if (target-num) in diff:
                return [diff[target-num], i]
            else:
                diff[num] = i
        
        return []