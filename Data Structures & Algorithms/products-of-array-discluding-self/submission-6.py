class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        [1,1,2,8]
        [1,6,24,48]
        """
        length = len(nums)
        res = [0]*length
        suffix = 1

        for i in range(length-1, -1, -1):
            res[i] = suffix
            suffix *= nums[i]
        
        prefix = 1
        for i in range(length):
            res[i] *= prefix
            prefix *= nums[i]
            
            
        return res

