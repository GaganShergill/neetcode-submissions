class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in mydict:
                return [mydict[c], i]
            else:
                mydict[num] = i
        return []