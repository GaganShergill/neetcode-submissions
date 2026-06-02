class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        l, r = 0, 1
        mcntr = cntr = 1
        seen = set(s[l])
        while r < len(s):
            if s[r] in seen:
                cntr = 1
                l += 1
                r = l
                seen = set(s[l])
            else:
                cntr += 1
                mcntr = max(mcntr, cntr)
                seen.add(s[r])
            r += 1
        
        return mcntr