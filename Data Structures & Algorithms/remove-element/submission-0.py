class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove the elements that are equal to val in the first pass
        # shift the elements left to fill the empty spaces
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
            else:
                k += 1
        
        x = 0
        for i in range(k):
            if nums[i] is not None:
                x += 1
                continue
            else:
                for j in range(x+1, len(nums)):
                    if nums[j] is not None:
                        nums[i] = nums[j]
                        nums[j] = None
                        x = j
                        break
        print(k)
        return k