class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newArray = []
        i = 0
        j = 0

        for _ in range(m+n):
            if i >= m:
                newArray.append(nums2[j])
                j += 1
            elif j >= n:
                newArray.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                newArray.append(nums1[i])
                i += 1
            else:
                newArray.append(nums2[j])
                j += 1
        
        for i in range(m+n):
            nums1[i] = newArray[i]
