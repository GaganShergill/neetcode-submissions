class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        p = [1]*length
        s = [1]*length
        for i in range(length):
            j = length - i - 1
            if i == 0:
                p[i] = nums[i]
                s[j] = nums[j]
                continue
            p[i] = p[i-1] * nums[i]
            s[j] = s[j+1] * nums[j]
        
        print(p,s)

        output = []
        for i in range(length):
            prefix = 1
            suffix = 1
            if i + 1 < length:
                suffix = s[i+1]
            
            if i - 1 >= 0:
                prefix = p[i-1]


            output.append(prefix*suffix)
        
        return output