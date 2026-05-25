class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt_c_ones = 0
        max_cnt_c_ones = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                cnt_c_ones = 0
            else:
                cnt_c_ones += 1
            
            if cnt_c_ones > max_cnt_c_ones:
                    max_cnt_c_ones = cnt_c_ones

        
        return max_cnt_c_ones