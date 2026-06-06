class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = [0]*26
        for c in s:
            idx = ord(c)-ord('a')
            arr[idx]  += 1
        
        for c in t:
            idx = ord(c)-ord('a')
            if arr[idx] == 0:
                return False
            else:
                arr[idx] -= 1
        
        return True
