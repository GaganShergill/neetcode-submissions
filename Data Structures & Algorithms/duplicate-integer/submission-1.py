class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for num in nums:
            if num in freq:
                return True
            else:
                freq.add(num)

        return False