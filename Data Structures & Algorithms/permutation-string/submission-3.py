class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = Counter(s1)
        left = 0
        length = 0
        for right in range(len(s2)):
            c = s2[right]

            if c in s1_dict and s1_dict[c] > 0:
                s1_dict[c] -= 1
                length += 1
            elif c in s1_dict:
                while s1_dict[c] <= 0:
                    s1_dict[s2[left]] += 1
                    length -= 1
                    left += 1
                s1_dict[c] -= 1
                length += 1
            else:
                while left < right + 1:
                    if s2[left] in s1_dict:
                        s1_dict[s2[left]] += 1
                        length -= 1
                    left += 1
            
            if length == len(s1):
                return True
        
        return False
