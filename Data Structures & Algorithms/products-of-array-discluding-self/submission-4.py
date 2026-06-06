class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        [1,1,2,8,48]
        [48,48,24,6,1]
        [1,6,24,48,48] <=> [48,48,24,6,1]
        """
        rpl = [1]
        for i in range(len(nums)-1):
            num = nums[i]
            rpl.append(rpl[-1]*num)
        
        rpr = [1]
        for i in range(len(nums)-1,0,-1):
            num = nums[i]
            rpr.append(rpr[-1]*num)
        
        l = len(nums)
        res = []

        for i in range(l):
            j = l-i-1
            res.append(rpl[i]*rpr[j])
        
        return res





