class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = len(sorted_nums)-1
        pair = set()
        while i < j:
            if sorted_nums[i]+sorted_nums[j] > target:
                j -= 1
            elif sorted_nums[i]+sorted_nums[j] < target:
                i += 1
            else:
                pair.add(sorted_nums[i])
                pair.add(sorted_nums[j])
                break
        
        res = []
        for idx in range(len(nums)):
            if len(res) == 2:
                break
            elif nums[idx] in pair:
                res.append(idx)
        
        return res
