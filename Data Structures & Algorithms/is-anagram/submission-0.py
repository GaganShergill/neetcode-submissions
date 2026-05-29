from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cntr = Counter(s)
        for c in t:
            if c not in cntr:
                return False
            elif cntr[c] < 1:
                return False
            else:
                cntr[c] -= 1
        
        return True