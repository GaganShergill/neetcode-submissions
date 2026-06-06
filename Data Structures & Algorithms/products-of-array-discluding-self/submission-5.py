class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        [1,1,2,8]
        [1,6,24,48]
        """
        length = len(nums)

        prefix = [1]
        for i in range(length-1):
            num = nums[i]
            prefix.append(prefix[-1]*num)
        
        suffix = [1]
        for i in range(length-1,0,-1):
            num = nums[i]
            suffix.append(suffix[-1]*num)
        
        
        res = []

        for i in range(length):
            j = length-i-1
            res.append(prefix[i]*suffix[j])
        
        return res





